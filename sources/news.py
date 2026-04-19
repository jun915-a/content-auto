import requests
from typing import List
from .base import TrendSource, TrendItem


class HackerNewsSource(TrendSource):
    """Hacker News トップストーリー（無料・認証不要）"""
    name = "hackernews"

    def fetch(self, limit: int = 10) -> List[TrendItem]:
        items = []
        try:
            top_ids = requests.get(
                "https://hacker-news.firebaseio.com/v0/topstories.json",
                timeout=10
            ).json()[:limit * 2]

            for story_id in top_ids:
                try:
                    story = requests.get(
                        f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json",
                        timeout=10
                    ).json()

                    if not story or story.get("type") != "story":
                        continue

                    items.append(TrendItem(
                        title=story.get("title", ""),
                        url=story.get("url", f"https://news.ycombinator.com/item?id={story_id}"),
                        source="hackernews",
                        score=story.get("score", 0),
                        description=story.get("text", "")[:500],
                    ))

                    if len(items) >= limit:
                        break
                except Exception:
                    continue

        except Exception as e:
            print(f"[ERROR] HackerNews: {e}")

        return sorted(items, key=lambda x: x.score, reverse=True)
