import json
import os
from datetime import datetime
from typing import List, Dict

HISTORY_FILE = "published_history.json"


def load_history() -> List[Dict]:
    if not os.path.exists(HISTORY_FILE):
        return []
    try:
        with open(HISTORY_FILE) as f:
            data = json.load(f)
            if not isinstance(data, list):
                print(f"[WARN] {HISTORY_FILE} is not a list, resetting")
                return []
            return data
    except Exception as e:
        print(f"[WARN] Failed to load {HISTORY_FILE}: {e}")
        return []


def save_entry(title: str, url: str, source: str, tags: List[str]):
    history = load_history()
    history.append({
        "timestamp": datetime.now().isoformat(),
        "title": title,
        "url": url,
        "source": source,
        "tags": tags,
    })
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)


def is_duplicate_source(source_url: str) -> bool:
    """過去に同じソースから記事生成済みかチェック"""
    history = load_history()
    for entry in history:
        if entry.get("source") == source_url:
            return True
    return False
