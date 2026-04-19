from datetime import datetime
from config import ARTICLES_PER_DAY, REDDIT_SUBREDDITS
from sources import RedditSource, HackerNewsSource
from generators import ArticleGenerator
from publishers import BloggerPublisher
from notifier import send_discord
from tracker import save_entry, is_duplicate_source
from article_storage import save_article, commit_articles, cleanup_old_articles


def collect_trends() -> list:
    """複数ソースからトレンドを収集"""
    sources = [
        HackerNewsSource(),
    ]
    # Reddit は GitHub Actions で ブロックされることがあるのでオプション
    try:
        sources.append(RedditSource(REDDIT_SUBREDDITS))
    except Exception:
        pass

    all_trends = []
    for source in sources:
        try:
            print(f"[INFO] {source.name} 取得中...")
            trends = source.fetch(limit=10)
            print(f"  {len(trends)}件取得")
            all_trends.extend(trends)
        except Exception as e:
            print(f"[WARN] {source.name} 取得失敗: {e}")

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
    publisher = BloggerPublisher()

    published = 0
    for trend in trends:
        if published >= ARTICLES_PER_DAY:
            break

        print(f"\n[{published + 1}/{ARTICLES_PER_DAY}] 生成中: {trend.title[:60]}...")

        ja_article, en_article = generator.generate(trend)
        if not ja_article or not en_article:
            print("  → 生成失敗、次へ")
            continue

        print(f"  日本語タイトル: {ja_article.title}")
        print(f"  英語タイトル: {en_article.title}")

        # 日本語版を Blogger へ投稿
        result = publisher.publish(ja_article, image_path=None)

        # 記事を GitHub に保存
        storage = save_article(
            ja_article.to_markdown(),
            en_article.to_markdown(),
            ja_article.title,
            en_article.title,
        )

        if result.success:
            save_entry(ja_article.title, result.url, trend.url, ja_article.tags)
            send_discord(f"✅ Blogger 投稿成功\n**{ja_article.title}**\n{result.url}")
            send_discord(f"📝 Note用（日本語）\n{ja_article.title}\n{storage['ja_url']}")
            send_discord(f"📝 Medium/Substack/Hashnode用（英語）\n{en_article.title}\n{storage['en_url']}")
            print(f"  → Blogger 投稿成功")
            published += 1
        else:
            print(f"  → Blogger 投稿失敗: {result.error}")
            send_discord(f"❌ Blogger 投稿失敗\n{ja_article.title}")
            send_discord(f"📝 Note用（日本語）\n{ja_article.title}\n{storage['ja_url']}")
            send_discord(f"📝 Medium/Substack/Hashnode用（英語）\n{en_article.title}\n{storage['en_url']}")

    send_discord(f"📊 本日の実行完了: {published}/{ARTICLES_PER_DAY}件投稿")
    print(f"\n完了: {published}/{ARTICLES_PER_DAY}件\n")

    # 記事を GitHub に commit
    print("[GIT] 記事を保存中...")
    commit_articles()

    # 古い記事を削除
    print("[CLEANUP] 古い記事をチェック中...")
    cleanup_old_articles(max_articles=100)


if __name__ == "__main__":
    run()
