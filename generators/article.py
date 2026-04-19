import requests
import json
from dataclasses import dataclass
from typing import Optional
from config import GROQ_API_KEY, ARTICLE_TEMPLATE


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
        if not GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY が未設定です")
        self.api_key = GROQ_API_KEY
        self.model = "mixtral-8x7b-32768"

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
            url = "https://api.groq.com/openai/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            }
            payload = {
                "model": self.model,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7,
                "max_tokens": 2000,
            }

            res = requests.post(url, headers=headers, json=payload, timeout=30)

            if res.status_code != 200:
                error_data = res.json().get("error", {})
                error_msg = error_data.get("message", res.text)
                print(f"[ERROR] Groq API {res.status_code}: {error_msg[:200]}")
                return None

            data = res.json()
            text = data.get("choices", [{}])[0].get("message", {}).get("content", "")

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
