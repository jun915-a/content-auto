import requests
import json
from dataclasses import dataclass
from typing import Optional
from config import (
    GROQ_API_KEY,
    GEMINI_API_KEY,
    MISTRAL_API_KEY,
    TOGETHER_API_KEY,
    HF_API_TOKEN,
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


def _build_prompt(trend, language: str = "ja") -> str:
    lang_config = {
        "ja": {
            "title_hint": "日本語タイトル（60文字以内、インパクト重視）",
            "summary_hint": "冒頭要約（150-200文字、この記事を読むべき理由を明確に）",
            "section1": "このトピックの本質",
            "section2": "5秒で分かるポイント",
            "section3": "詳細解説",
            "section4": "実世界への影響",
            "section5": "結論",
            "marker1": "📌",
            "marker2": "🎯",
            "marker3": "📊",
            "marker4": "🚀",
            "marker5": "✨",
        },
        "en": {
            "title_hint": "English title (max 70 chars, impactful)",
            "summary_hint": "Summary (150-200 chars, hook the reader)",
            "section1": "The Core of This Topic",
            "section2": "5-Second Key Points",
            "section3": "Detailed Breakdown",
            "section4": "Real-World Impact",
            "section5": "Conclusion",
            "marker1": "🔑",
            "marker2": "⚡",
            "marker3": "📈",
            "marker4": "🎯",
            "marker5": "✨",
        }
    }

    cfg = lang_config.get(language, lang_config["ja"])

    return f"""Topic: {trend.title}
URL: {trend.url}
Description: {trend.description[:200]}

Generate a {language.upper()} article in JSON format. Return ONLY JSON.
**Prioritize visual clarity and readability.**

{{
  "title": "{cfg['title_hint']}",
  "summary": "{cfg['summary_hint']}",
  "details": "Markdown article (1000-1500 chars with this structure):

## {cfg['marker1']} {cfg['section1']}
[200 chars explaining the core issue/context]

---

## {cfg['marker2']} {cfg['section2']}
- ✓ Point 1
- ✓ Point 2
- ✓ Point 3

---

## {cfg['marker3']} {cfg['section3']}

### 1. [Key Element 1]
[~150 chars]

| Aspect | Description |
|--------|-------------|
| A | [Detail] |
| B | [Detail] |

### 2. [Key Element 2]
[~150 chars]

> 💡 **Insight**: [Important takeaway]

### 3. [Key Element 3]
[~150 chars]

---

## {cfg['marker4']} {cfg['section4']}
- Impact 1
- Impact 2
- Impact 3

---

## {cfg['marker5']} {cfg['section5']}
[Closing message & next action]",
  "tags": ["tag1", "tag2", "tag3"]
}}"""


def _parse_article(text: str, trend) -> Optional[Article]:
    if "```json" in text:
        text = text.split("```json")[1].split("```")[0].strip()
    elif "```" in text:
        text = text.split("```")[1].split("```")[0].strip()

    # JSON部分を抽出（先頭の { から最後の } まで）
    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1:
        text = text[start:end + 1]

    try:
        import re
        # JSONの値内の改行をエスケープ（"..." の中の改行を \n に）
        def escape_json_value(match):
            return match.group(0).replace('\n', '\\n').replace('\r', '\\r').replace('\t', '\\t')
        text = re.sub(r'"[^"]*"', escape_json_value, text)

        data = json.loads(text)
        return Article(
            title=data.get("title", trend.title),
            summary=data.get("summary", ""),
            details=data.get("details", ""),
            tags=data.get("tags", []),
            source_url=trend.url,
        )
    except Exception as e:
        print(f"  [WARN] JSON parse失敗: {e}")
        print(f"  [DEBUG] 受信テキスト: {text[:300]}")
        return None


def _call_groq(prompt: str) -> Optional[str]:
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
                "model": "llama-3.3-70b-versatile",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7,
                "max_tokens": 2000,
            },
            timeout=30,
        )
        if res.status_code != 200:
            print(f"  [Groq] {res.status_code}: {res.text[:200]}")
            return None
        return res.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"  [Groq] 例外: {e}")
        return None


def _call_gemini(prompt: str) -> Optional[str]:
    if not GEMINI_API_KEY:
        return None
    models = ["gemini-2.0-flash", "gemini-2.5-flash", "gemini-1.5-flash"]
    for model in models:
        try:
            res = requests.post(
                f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",
                headers={"Content-Type": "application/json"},
                params={"key": GEMINI_API_KEY},
                json={
                    "contents": [{"parts": [{"text": prompt}]}],
                    "generationConfig": {"temperature": 0.7, "maxOutputTokens": 2000},
                },
                timeout=30,
            )
            if res.status_code == 200:
                candidates = res.json().get("candidates", [])
                if candidates:
                    return candidates[0]["content"]["parts"][0].get("text", "")
            else:
                print(f"  [Gemini:{model}] {res.status_code}: {res.text[:150]}")
        except Exception as e:
            print(f"  [Gemini:{model}] 例外: {e}")
    return None


def _call_mistral(prompt: str) -> Optional[str]:
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
                "model": "mistral-large-latest",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7,
                "max_tokens": 2000,
            },
            timeout=30,
        )
        if res.status_code != 200:
            print(f"  [Mistral] {res.status_code}: {res.text[:200]}")
            return None
        return res.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"  [Mistral] 例外: {e}")
        return None


def _call_together(prompt: str) -> Optional[str]:
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
                "model": "meta-llama/Llama-3-70b-chat-hf",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7,
                "max_tokens": 2000,
            },
            timeout=30,
        )
        if res.status_code != 200:
            print(f"  [Together] {res.status_code}: {res.text[:200]}")
            return None
        return res.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"  [Together] 例外: {e}")
        return None


def _call_hf(prompt: str) -> Optional[str]:
    if not HF_API_TOKEN:
        return None
    try:
        res = requests.post(
            "https://api-inference.huggingface.co/models/meta-llama/Llama-2-70b-chat-hf",
            headers={"Authorization": f"Bearer {HF_API_TOKEN}"},
            json={"inputs": prompt},
            timeout=30,
        )
        if res.status_code != 200:
            print(f"  [HF] {res.status_code}: {res.text[:200]}")
            return None
        result = res.json()
        if isinstance(result, list) and len(result) > 0:
            return result[0].get("generated_text", "")
        return None
    except Exception as e:
        print(f"  [HF] 例外: {e}")
        return None


def _call_cohere(prompt: str) -> Optional[str]:
    if not COHERE_API_KEY:
        return None
    try:
        res = requests.post(
            "https://api.cohere.ai/v1/generate",
            headers={
                "Authorization": f"Bearer {COHERE_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "prompt": prompt,
                "temperature": 0.7,
                "max_tokens": 2000,
            },
            timeout=30,
        )
        if res.status_code != 200:
            print(f"  [Cohere] {res.status_code}: {res.text[:200]}")
            return None
        generations = res.json().get("generations", [])
        if generations:
            return generations[0].get("text", "")
        return None
    except Exception as e:
        print(f"  [Cohere] 例外: {e}")
        return None


class ArticleGenerator:
    def __init__(self):
        if not GROQ_API_KEY and not GEMINI_API_KEY:
            raise ValueError("GROQ_API_KEY か GEMINI_API_KEY のどちらかが必要です")

    def _generate_one(self, trend, language: str = "ja") -> Optional[Article]:
        prompt = _build_prompt(trend, language)

        # フォールバック順: Groq → Gemini → Mistral → Together → HF → Cohere
        llm_calls = [
            ("Groq", _call_groq),
            ("Gemini", _call_gemini),
            ("Mistral", _call_mistral),
            ("Together", _call_together),
            ("HuggingFace", _call_hf),
            ("Cohere", _call_cohere),
        ]

        for name, call_func in llm_calls:
            text = call_func(prompt)
            if text:
                article = _parse_article(text, trend)
                if article:
                    print(f"  [LLM] {name} で生成成功")
                    return article

        print("  [LLM] 全て失敗")
        return None

    def generate(self, trend) -> tuple[Optional[Article], Optional[Article]]:
        """日本語版と英語版を同時生成"""
        print("  [LLM] 日本語版生成中...")
        ja_article = self._generate_one(trend, "ja")
        if ja_article:
            print("  [LLM] 日本語版成功")
        else:
            print("  [LLM] 日本語版失敗")

        print("  [LLM] 英語版生成中...")
        en_article = self._generate_one(trend, "en")
        if en_article:
            print("  [LLM] 英語版成功")
        else:
            print("  [LLM] 英語版失敗")

        return ja_article, en_article
