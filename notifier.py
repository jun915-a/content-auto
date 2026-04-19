import requests
from config import DISCORD_WEBHOOK_URL


def send_discord(message: str):
    if not DISCORD_WEBHOOK_URL:
        print("[WARN] DISCORD_WEBHOOK_URL が未設定")
        return
    try:
        requests.post(DISCORD_WEBHOOK_URL, json={"content": message}, timeout=10)
    except Exception as e:
        print(f"[ERROR] Discord通知失敗: {e}")
