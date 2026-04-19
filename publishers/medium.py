import requests
from typing import Optional
from config import MEDIUM_API_TOKEN, MEDIUM_USER_ID
from .base import Publisher, PublishResult


class MediumPublisher(Publisher):
    name = "medium"
    API_BASE = "https://api.medium.com/v1"

    def publish(self, article, image_path: Optional[str] = None) -> PublishResult:
        if not MEDIUM_API_TOKEN or not MEDIUM_USER_ID:
            return PublishResult(
                success=False,
                error="MEDIUM_API_TOKEN または MEDIUM_USER_ID が未設定",
            )

        headers = {
            "Authorization": f"Bearer {MEDIUM_API_TOKEN}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        content = article.to_markdown()

        # 画像があれば冒頭に追加
        if image_path:
            image_url = self._upload_image(image_path, headers)
            if image_url:
                content = f"![{article.title}]({image_url})\n\n" + content

        payload = {
            "title": article.title,
            "contentFormat": "markdown",
            "content": content,
            "tags": article.tags[:5],
            "publishStatus": "public",
            "canonicalUrl": article.source_url,
        }

        try:
            res = requests.post(
                f"{self.API_BASE}/users/{MEDIUM_USER_ID}/posts",
                headers=headers,
                json=payload,
                timeout=30,
            )
            if res.status_code == 201:
                data = res.json().get("data", {})
                return PublishResult(success=True, url=data.get("url", ""))
            else:
                return PublishResult(
                    success=False,
                    error=f"Medium API {res.status_code}: {res.text[:200]}",
                )
        except Exception as e:
            return PublishResult(success=False, error=str(e))

    def _upload_image(self, image_path: str, headers: dict) -> Optional[str]:
        try:
            upload_headers = {"Authorization": headers["Authorization"]}
            with open(image_path, "rb") as f:
                res = requests.post(
                    f"{self.API_BASE}/images",
                    headers=upload_headers,
                    files={"image": (image_path, f, "image/png")},
                    timeout=30,
                )
            if res.status_code == 201:
                return res.json().get("data", {}).get("url")
        except Exception as e:
            print(f"[WARN] 画像アップロード失敗: {e}")
        return None
