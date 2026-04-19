import requests
from typing import Optional
from config import BLOGGER_API_KEY, BLOGGER_BLOG_ID
from .base import Publisher, PublishResult


class BloggerPublisher(Publisher):
    name = "blogger"
    API_BASE = "https://www.googleapis.com/blogger/v3"

    def publish(self, article, image_path: Optional[str] = None) -> PublishResult:
        if not BLOGGER_API_KEY or not BLOGGER_BLOG_ID:
            import os
            print(f"  [DEBUG] env BLOGGER_API_KEY: {os.environ.get('BLOGGER_API_KEY', 'NOT_IN_ENV')[:20]}")
            print(f"  [DEBUG] env BLOGGER_BLOG_ID: {os.environ.get('BLOGGER_BLOG_ID', 'NOT_IN_ENV')}")
            print(f"  [DEBUG] config BLOGGER_API_KEY: {BLOGGER_API_KEY[:20] if BLOGGER_API_KEY else 'EMPTY'}")
            print(f"  [DEBUG] config BLOGGER_BLOG_ID: {BLOGGER_BLOG_ID if BLOGGER_BLOG_ID else 'EMPTY'}")
            return PublishResult(
                success=False,
                error="BLOGGER_API_KEY または BLOGGER_BLOG_ID が未設定",
            )

        content = article.to_markdown()

        # 画像があれば冒頭に追加
        if image_path:
            content = f"![{article.title}](file://{image_path})\n\n" + content

        payload = {
            "kind": "blogger#post",
            "title": article.title,
            "content": content,
            "labels": article.tags,
        }

        try:
            url = f"{self.API_BASE}/blogs/{BLOGGER_BLOG_ID}/posts"
            res = requests.post(
                url,
                headers={"Content-Type": "application/json"},
                params={"key": BLOGGER_API_KEY},
                json=payload,
                timeout=30,
            )

            if res.status_code == 201:
                data = res.json()
                post_url = data.get("url", "")
                return PublishResult(success=True, url=post_url)
            else:
                try:
                    error_data = res.json().get("error", {})
                    error_msg = error_data.get("message", res.text)
                except:
                    error_msg = res.text
                print(f"  [DEBUG] Blogger API Error: {res.status_code}")
                print(f"  [DEBUG] Full response: {res.text[:500]}")
                return PublishResult(
                    success=False,
                    error=f"Blogger API {res.status_code}: {error_msg[:200]}",
                )
        except Exception as e:
            return PublishResult(success=False, error=str(e))
