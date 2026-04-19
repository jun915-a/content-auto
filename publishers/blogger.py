import requests
from typing import Optional
from config import SENDGRID_API_KEY, BLOGGER_BLOG_EMAIL, SENDGRID_FROM_EMAIL
from .base import Publisher, PublishResult


class BloggerPublisher(Publisher):
    name = "blogger"
    SENDGRID_API = "https://api.sendgrid.com/v3/mail/send"

    def publish(self, article, image_path: Optional[str] = None) -> PublishResult:
        if not SENDGRID_API_KEY or not BLOGGER_BLOG_EMAIL:
            return PublishResult(
                success=False,
                error="SENDGRID_API_KEY または BLOGGER_BLOG_EMAIL が未設定",
            )

        content = article.to_markdown()
        subject = article.title

        payload = {
            "personalizations": [{"to": [{"email": BLOGGER_BLOG_EMAIL}]}],
            "from": {"email": SENDGRID_FROM_EMAIL, "name": "Content Auto"},
            "subject": subject,
            "content": [{"type": "text/html", "value": content}],
        }

        try:
            res = requests.post(
                self.SENDGRID_API,
                headers={
                    "Authorization": f"Bearer {SENDGRID_API_KEY}",
                    "Content-Type": "application/json",
                },
                json=payload,
                timeout=30,
            )

            if res.status_code in (200, 201, 202):
                return PublishResult(
                    success=True,
                    url="https://www.blogger.com (Posted via email)",
                )
            else:
                print(f"  [DEBUG] SendGrid Error: {res.status_code}")
                print(f"  [DEBUG] Response: {res.text[:300]}")
                return PublishResult(
                    success=False,
                    error=f"SendGrid {res.status_code}: {res.text[:100]}",
                )
        except Exception as e:
            return PublishResult(success=False, error=str(e))
