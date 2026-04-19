import requests
import json
from dataclasses import dataclass
from typing import Optional
from config import GEMINI_API_KEY, ARTICLE_TEMPLATE


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


class ArticleGenerator:
    def __init__(self):
        if not GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY が未設定です")
        self.api_key = GEMINI_API_KEY

    def generate(self, trend) -> Optional[Article]:
        prompt = f"""
以下のトピックについて、日本語のブログ記事を書いてください。

トピック: {trend.title}
参照URL: {trend.url}
補足: {trend.description[:300]}

フォーマット（JSONで返してください）:
{{
  "title": "魅力的な日本語タイトル（60文字以内）",
  "summary": "1-2段落の要約（200-300文字）。読者がこの記事を読みたくなるフック",
  "details": "詳細セクション（500-800文字）。マークダウン形式。H2やリストを使って読みやすく",
  "tags": ["タグ1", "タグ2", "タグ3"]
}}

重要:
- SEO最適化（検索されそうなキーワードを自然に含める）
- 読みやすい日本語
- 簡潔だが詳しい情報
"""

        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
            headers = {"Content-Type": "application/json"}
            payload = {
                "contents": [{"parts": [{"text": prompt}]}],
                "generationConfig": {
                    "temperature": 0.7,
                    "topK": 40,
                    "topP": 0.95,
                },
            }

            res = requests.post(
                url,
                headers=headers,
                params={"key": self.api_key},
                json=payload,
                timeout=30,
            )

            if res.status_code != 200:
                print(f"[ERROR] Gemini API {res.status_code}: {res.text[:200]}")
                return None

            data = res.json()
            candidates = data.get("candidates", [])
            if not candidates:
                return None

            text = candidates[0].get("content", {}).get("parts", [{}])[0].get("text", "")

            # JSONを抽出
            if "```json" in text:
                text = text.split("```json")[1].split("```")[0].strip()
            elif "```" in text:
                text = text.split("```")[1].split("```")[0].strip()

            article_data = json.loads(text)

            return Article(
                title=article_data.get("title", trend.title),
                summary=article_data.get("summary", ""),
                details=article_data.get("details", ""),
                tags=article_data.get("tags", []),
                source_url=trend.url,
            )
        except Exception as e:
            print(f"[ERROR] 記事生成失敗: {e}")
            return None
