import requests
from typing import List
from .base import TrendSource, TrendItem


class RedditSource(TrendSource):
    name = "reddit"

    def __init__(self, subreddits: List[str]):
        self.subreddits = subreddits

    def fetch(self, limit: int = 10) -> List[TrendItem]:
        items = []
        headers = {"User-Agent": "content-auto:v1.0 (trend scanner)"}

        for sub in self.subreddits:
            url = f"https://www.reddit.com/r/{sub}/top.json?t=day&limit={limit}"
            try:
                res = requests.get(url, headers=headers, timeout=15)
                res.raise_for_status()
                data = res.json()

                for post in data.get("data", {}).get("children", []):
                    p = post.get("data", {})
                    items.append(TrendItem(
                        title=p.get("title", ""),
                        url=f"https://reddit.com{p.get('permalink', '')}",
                        source=f"reddit/r/{sub}",
                        score=p.get("score", 0),
                        description=p.get("selftext", "")[:500],
                    ))
            except Exception as e:
                print(f"[ERROR] Reddit r/{sub}: {e}")

        return sorted(items, key=lambda x: x.score, reverse=True)
