from datetime import datetime
from config import ARTICLES_PER_DAY, REDDIT_SUBREDDITS
from sources import RedditSource, HackerNewsSource
from generators import ArticleGenerator, ImageGenerator
from publishers import BloggerPublisher
from notifier import send_discord
from tracker import save_entry, is_duplicate_source


def collect_trends() -> list:
    """複数ソースからトレンドを収集"""
    sources = [
        HackerNewsSource(),
        RedditSource(REDDIT_SUBREDDITS),
    ]
    all_trends = []
    for source in sources:
        print(f"[INFO] {source.name} 取得中...")
        trends = source.fetch(limit=10)
        print(f"  {len(trends)}件取得")
        all_trends.extend(trends)

    # スコア順 + 重複除外
    unique = {}
    for t in all_trends:
        if not is_duplicate_source(t.url):
            unique[t.url] = t
    return sorted(unique.values(), key=lambda x: x.score, reverse=True)


def run():
    print(f"\n{'='*50}")
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M')}] 記事生成開始")
    print(f"{'='*50}\n")

    trends = collect_trends()
    print(f"\n候補トレンド: {len(trends)}件\n")

    if len(trends) == 0:
        send_discord("⚠️ トレンドが取得できませんでした")
        return

    generator = ArticleGenerator()
    image_gen = ImageGenerator()
    publisher = BloggerPublisher()

    published = 0
    for trend in trends:
        if published >= ARTICLES_PER_DAY:
            break

        print(f"\n[{published + 1}/{ARTICLES_PER_DAY}] 生成中: {trend.title[:60]}...")

        article = generator.generate(trend)
        if not article:
            print("  → 生成失敗、次へ")
            continue

        print(f"  タイトル: {article.title}")

        # 画像生成
        image_prompt = f"blog header image for article about {article.title}, modern minimalist style"
        image_path = image_gen.generate(image_prompt, f"image_{published}.png")

        # 投稿
        result = publisher.publish(article, image_path)

        if result.success:
            save_entry(article.title, result.url, trend.url, article.tags)
            send_discord(f"✅ 投稿完了\n**{article.title}**\n{result.url}")
            print(f"  → 投稿成功: {result.url}")
            published += 1
        else:
            print(f"  → 投稿失敗: {result.error}")
            send_discord(f"❌ 投稿失敗\n{article.title}\n{result.error}")

    send_discord(f"📊 本日の実行完了: {published}/{ARTICLES_PER_DAY}件投稿")
    print(f"\n完了: {published}/{ARTICLES_PER_DAY}件\n")


if __name__ == "__main__":
    run()
