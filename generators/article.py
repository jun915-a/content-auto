import requests
import json
import re
from dataclasses import dataclass
from typing import Optional, Callable, List, Tuple
from config import (
    GROQ_API_KEY,
    GEMINI_API_KEY,
    MISTRAL_API_KEY,
    TOGETHER_API_KEY,
    COHERE_API_KEY,
    ARTICLE_TEMPLATE,
)


@dataclass
class Article:
    title: str
    summary: str
    details: str
    tags: list
    source_url: str

    def to_markdown(self) -> str:
        return ARTICLE_TEMPLATE.format(
            summary=self.summary,
            details=self.details,
        )


_LANG_CONFIG = {
    "ja": {
        "title_hint": "日本語タイトル（60文字以内、インパクト重視）",
        "summary_hint": "冒頭要約（150-200文字、読む理由を明確に）",
        "sec1": "このトピックの本質",
        "sec2": "5秒で分かるポイント",
        "sec3": "詳細解説",
        "sec4": "実世界への影響",
        "sec5": "結論",
        "m": ["📌", "🎯", "📊", "🚀", "✨"],
    },
    "en": {
        "title_hint": "English title (max 70 chars, impactful)",
        "summary_hint": "Summary (150-200 chars, hook the reader)",
        "sec1": "The Core of This Topic",
        "sec2": "5-Second Key Points",
        "sec3": "Detailed Breakdown",
        "sec4": "Real-World Impact",
        "sec5": "Conclusion",
        "m": ["🔑", "⚡", "📈", "🎯", "✨"],
    },
}


def _build_prompt(trend, language: str = "ja") -> str:
    cfg = _LANG_CONFIG.get(language, _LANG_CONFIG["ja"])
    m = cfg["m"]

    # より簡潔なプロンプト（トークン節約）
    return f"""Topic: {trend.title}
URL: {trend.url}
Context: {trend.description[:200]}

Generate a {language.upper()} article. Return ONLY a valid JSON object with these exact fields:
- title: {cfg['title_hint']}
- summary: {cfg['summary_hint']}
- details: Markdown article 1000-1500 chars following this structure:
## {m[0]} {cfg['sec1']}
[200文字 core explanation]

## {m[1]} {cfg['sec2']}
- Point 1
- Point 2
- Point 3

## {m[2]} {cfg['sec3']}
### 1. [Element 1]
[~150 chars]

### 2. [Element 2]
[~150 chars]

> 💡 **Insight**: [takeaway]

## {m[3]} {cfg['sec4']}
- Impact 1
- Impact 2

## {m[4]} {cfg['sec5']}
[Closing]
- tags: array of 3 relevant tags

Output valid JSON only, no markdown fences, no extra text."""


def _extract_json(text: str) -> Optional[dict]:
    """LLM出力から JSON を抽出（複数戦略）"""
    if not text:
        return None

    # 戦略1: ```json ブロック
    m = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    if m:
        candidate = m.group(1)
        result = _try_parse(candidate)
        if result:
            return result

    # 戦略2: 最初の { から最後の } まで
    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1 and end > start:
        candidate = text[start:end + 1]
        result = _try_parse(candidate)
        if result:
            return result

    return None


def _try_parse(text: str) -> Optional[dict]:
    """複数戦略で JSON パースを試行"""
    # まずそのまま
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # 制御文字エスケープ
    try:
        # JSON文字列値内の改行をエスケープ
        fixed = re.sub(
            r'"((?:[^"\\]|\\.)*)"',
            lambda m: '"' + m.group(1).replace("\n", "\\n").replace("\r", "\\r").replace("\t", "\\t") + '"',
            text,
        )
        return json.loads(fixed)
    except json.JSONDecodeError:
        pass

    # 末尾が切れている場合は修復を試みる
    try:
        # 最後のカンマを削除
        cleaned = re.sub(r",\s*}", "}", text)
        cleaned = re.sub(r",\s*]", "]", cleaned)
        return json.loads(cleaned)
    except json.JSONDecodeError:
        pass

    return None


def _parse_article(text: str, trend) -> Optional[Article]:
    data = _extract_json(text)
    if not data:
        return None

    title = data.get("title", "").strip()
    details = data.get("details", "").strip()
    if not title or not details:
        return None

    return Article(
        title=title,
        summary=data.get("summary", "").strip(),
        details=details,
        tags=data.get("tags", []) if isinstance(data.get("tags"), list) else [],
        source_url=trend.url,
    )


# ======== LLM呼び出し ========

def _call_groq(prompt: str, model: str = "llama-3.3-70b-versatile") -> Optional[str]:
    """Groq API（JSON mode対応）"""
    if not GROQ_API_KEY:
        return None
    try:
        res = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": model,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7,
                "max_tokens": 1500,
                "response_format": {"type": "json_object"},
            },
            timeout=30,
        )
        if res.status_code == 429:
            return None  # レート制限は静かにスキップ
        if res.status_code != 200:
            print(f"  [Groq:{model}] {res.status_code}: {res.text[:150]}")
            return None
        return res.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"  [Groq:{model}] 例外: {e}")
        return None


def _call_gemini(prompt: str, model: str) -> Optional[str]:
    """Gemini API（JSON mode対応）"""
    if not GEMINI_API_KEY:
        return None
    try:
        res = requests.post(
            f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",
            headers={"Content-Type": "application/json"},
            params={"key": GEMINI_API_KEY},
            json={
                "contents": [{"parts": [{"text": prompt}]}],
                "generationConfig": {
                    "temperature": 0.7,
                    "maxOutputTokens": 1500,
                    "responseMimeType": "application/json",
                },
            },
            timeout=30,
        )
        if res.status_code == 429:
            return None
        if res.status_code != 200:
            print(f"  [Gemini:{model}] {res.status_code}: {res.text[:150]}")
            return None
        candidates = res.json().get("candidates", [])
        if candidates:
            return candidates[0]["content"]["parts"][0].get("text", "")
        return None
    except Exception as e:
        print(f"  [Gemini:{model}] 例外: {e}")
        return None


def _call_mistral(prompt: str, model: str = "mistral-small-latest") -> Optional[str]:
    """Mistral API（JSON mode対応）"""
    if not MISTRAL_API_KEY:
        return None
    try:
        res = requests.post(
            "https://api.mistral.ai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {MISTRAL_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": model,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7,
                "max_tokens": 1500,
                "response_format": {"type": "json_object"},
            },
            timeout=45,
        )
        if res.status_code == 429:
            return None
        if res.status_code != 200:
            print(f"  [Mistral:{model}] {res.status_code}: {res.text[:150]}")
            return None
        return res.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"  [Mistral:{model}] 例外: {e}")
        return None


def _call_together(prompt: str, model: str = "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free") -> Optional[str]:
    """Together AI（無料モデル）"""
    if not TOGETHER_API_KEY:
        return None
    try:
        res = requests.post(
            "https://api.together.xyz/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {TOGETHER_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": model,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7,
                "max_tokens": 1500,
            },
            timeout=45,
        )
        if res.status_code in (402, 429):
            return None  # 課金切れ/レート制限は静かに
        if res.status_code != 200:
            print(f"  [Together:{model}] {res.status_code}: {res.text[:150]}")
            return None
        return res.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"  [Together:{model}] 例外: {e}")
        return None


def _call_cohere(prompt: str) -> Optional[str]:
    """Cohere v2 Chat API（2025年9月以降の新API）"""
    if not COHERE_API_KEY:
        return None
    try:
        res = requests.post(
            "https://api.cohere.com/v2/chat",
            headers={
                "Authorization": f"Bearer {COHERE_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": "command-r-08-2024",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7,
                "max_tokens": 1500,
                "response_format": {"type": "json_object"},
            },
            timeout=45,
        )
        if res.status_code == 429:
            return None
        if res.status_code != 200:
            print(f"  [Cohere] {res.status_code}: {res.text[:150]}")
            return None
        data = res.json()
        # v2 API レスポンス形式
        content = data.get("message", {}).get("content", [])
        if content and isinstance(content, list):
            return content[0].get("text", "")
        return None
    except Exception as e:
        print(f"  [Cohere] 例外: {e}")
        return None


# ======== フォールバックチェーン ========

def _build_fallback_chain() -> List[Tuple[str, Callable[[str], Optional[str]]]]:
    """
    優先順位：
    1. Groq 70B（最高品質、日次100kトークン）
    2. Groq 8B（8Bは別レート枠、高速）
    3. Gemini 2.5 Flash（無料枠が広い）
    4. Gemini 2.0 Flash
    5. Gemini 2.5 Flash Lite（より高いレート）
    6. Mistral Small（無料枠あり）
    7. Together（無料モデル）
    8. Cohere v2（トライアルキーで使える）
    """
    return [
        ("Groq-70B", lambda p: _call_groq(p, "llama-3.3-70b-versatile")),
        ("Groq-8B", lambda p: _call_groq(p, "llama-3.1-8b-instant")),
        ("Gemini-2.5-flash", lambda p: _call_gemini(p, "gemini-2.5-flash")),
        ("Gemini-2.0-flash", lambda p: _call_gemini(p, "gemini-2.0-flash")),
        ("Gemini-2.5-flash-lite", lambda p: _call_gemini(p, "gemini-2.5-flash-lite")),
        ("Mistral-small", lambda p: _call_mistral(p, "mistral-small-latest")),
        ("Mistral-8b", lambda p: _call_mistral(p, "ministral-8b-latest")),
        ("Together-free", lambda p: _call_together(p, "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free")),
        ("Cohere-v2", lambda p: _call_cohere(p)),
    ]


class ArticleGenerator:
    def __init__(self):
        if not any([GROQ_API_KEY, GEMINI_API_KEY, MISTRAL_API_KEY, COHERE_API_KEY, TOGETHER_API_KEY]):
            raise ValueError("少なくとも 1 つの LLM API キーが必要です")
        self.chain = _build_fallback_chain()

    def _generate_one(self, trend, language: str = "ja") -> Optional[Article]:
        prompt = _build_prompt(trend, language)

        for name, call_func in self.chain:
            text = call_func(prompt)
            if not text:
                continue

            article = _parse_article(text, trend)
            if article:
                print(f"  [LLM] {name} で生成成功")
                return article
            else:
                print(f"  [LLM] {name} → JSON parse失敗（次へ）")

        print("  [LLM] 全て失敗")
        return None

    def generate(self, trend) -> tuple[Optional[Article], Optional[Article]]:
        """日本語版と英語版を同時生成"""
        print("  [LLM] 日本語版生成中...")
        ja_article = self._generate_one(trend, "ja")

        print("  [LLM] 英語版生成中...")
        en_article = self._generate_one(trend, "en")

        return ja_article, en_article
