import requests
from typing import Optional
from config import HF_API_TOKEN


class ImageGenerator:
    """Hugging Face Inference API で無料画像生成"""

    MODEL_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"

    def __init__(self):
        self.headers = {"Authorization": f"Bearer {HF_API_TOKEN}"} if HF_API_TOKEN else {}

    def generate(self, prompt: str, output_path: str = "article_image.png") -> Optional[str]:
        if not HF_API_TOKEN:
            print("[WARN] HF_API_TOKEN 未設定のため画像生成をスキップ")
            return None

        try:
            res = requests.post(
                self.MODEL_URL,
                headers=self.headers,
                json={"inputs": prompt},
                timeout=60,
            )
            if res.status_code == 200:
                with open(output_path, "wb") as f:
                    f.write(res.content)
                return output_path
            else:
                print(f"[WARN] 画像生成失敗 ({res.status_code}): {res.text[:200]}")
                return None
        except Exception as e:
            print(f"[ERROR] 画像生成エラー: {e}")
            return None
