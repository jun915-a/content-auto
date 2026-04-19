import requests
import json
from dataclasses import dataclass
from typing import Optional
from config import GROQ_API_KEY, GEMINI_API_KEY, ARTICLE_TEMPLATE


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


def _build_prompt(trend) -> str:
    return f"""トピック: {trend.title}
URL: {trend.url}
説明: {trend.description[:200]}

以下のJSON形式で日本語記事を作成してください。JSONのみを返してください。
詳細は見やすさを最優先に、表・リスト・コードブロックを活用してください。

{{
  "title": "日本語タイトル（60文字以内）",
  "summary": "要約（200-300文字、読者が記事を読みたくなるフック）",
  "details": "詳細セクション（800-1200文字、マークダウン形式、以下の構造を推奨）
## 概要
段落1-2

## 主要ポイント
- ポイント1
- ポイント2
- ポイント3

## 詳細解説
|項目|説明|
|---|---|
|A|説明A|
|B|説明B|

## メリット・活用例
- 例1
- 例2

## まとめ
結論",
  "tags": ["タグ1", "タグ2", "タグ3"]
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
    # 複数モデルを順に試行
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


class ArticleGenerator:
    def __init__(self):
        if not GROQ_API_KEY and not GEMINI_API_KEY:
            raise ValueError("GROQ_API_KEY か GEMINI_API_KEY のどちらかが必要です")

    def generate(self, trend) -> Optional[Article]:
        prompt = _build_prompt(trend)

        # プライマリ: Groq
        print("  [LLM] Groq 試行中...")
        text = _call_groq(prompt)
        if text:
            article = _parse_article(text, trend)
            if article:
                print("  [LLM] Groq で生成成功")
                return article

        # フォールバック: Gemini
        print("  [LLM] Gemini にフォールバック...")
        text = _call_gemini(prompt)
        if text:
            article = _parse_article(text, trend)
            if article:
                print("  [LLM] Gemini で生成成功")
                return article

        print("  [LLM] 両方失敗")
        return None
