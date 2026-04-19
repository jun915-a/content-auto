from google import genai
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
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.model_name = "gemini-2.0-flash-exp"

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
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt,
            )
            text = response.text.strip()

            if "```json" in text:
                text = text.split("```json")[1].split("```")[0].strip()
            elif "```" in text:
                text = text.split("```")[1].split("```")[0].strip()

            import json
            data = json.loads(text)

            return Article(
                title=data.get("title", trend.title),
                summary=data.get("summary", ""),
                details=data.get("details", ""),
                tags=data.get("tags", []),
                source_url=trend.url,
            )
        except Exception as e:
            print(f"[ERROR] 記事生成失敗: {e}")
            return None
