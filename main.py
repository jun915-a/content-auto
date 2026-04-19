from datetime import datetime
from config import ARTICLES_PER_DAY, REDDIT_SUBREDDITS
from sources import RedditSource, HackerNewsSource
from generators import ArticleGenerator
from publishers import BloggerPublisher
from notifier import send_discord
from tracker import save_entry, is_duplicate_source
from article_storage import save_article, commit_articles, cleanup_old_articles
from trend_ranker import rank_trends


def collect_trends() -> list:
    """複数ソースからトレンドを収集 → バズ度で厳選"""
    sources = [
        HackerNewsSource(),
    ]
    # Reddit は GitHub Actions で ブロックされることがあるのでオプション
    try:
        sources.append(RedditSource(REDDIT_SUBREDDITS))
    except Exception as e:
        print(f"[WARN] Reddit ソース初期化失敗: {e}")

    all_trends = []
    for source in sources:
        try:
            print(f"[INFO] {source.name} 取得中...")
            trends = source.fetch(limit=30)  # 多めに取得してから厳選
            print(f"  {len(trends)}件取得")
            all_trends.extend(trends)
        except Exception as e:
            print(f"[WARN] {source.name} 取得失敗: {e}")

    # 重複除外
    unique = {}
    for t in all_trends:
        if not is_duplicate_source(t.url):
            unique[t.url] = t

    # バズ度でランキング
    ranked = rank_trends(list(unique.values()), min_score=10)
    print(f"[INFO] {len(unique)}件 → バズ度フィルタ後 {len(ranked)}件")

    # 上位の概要を表示
    for i, t in enumerate(ranked[:10]):
        print(f"  #{i+1} [バズ度:{t.virality_score}] {t.title[:60]}")

    return ranked


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
            send_discord(f"""📝 Note用（日本語）
{ja_article.title}

**Note風（綺麗版）:** {storage['ja_formatted_url']}
**シンプルmd:** {storage['ja_simple_url']}

**ここから投稿してください:**
https://note.com/""")
            send_discord(f"""📝 Medium/Substack/Hashnode用（英語）
{en_article.title}

**Note風（綺麗版）:** {storage['en_formatted_url']}
**シンプルmd:** {storage['en_simple_url']}

**Medium: https://medium.com/new-story**
**Substack: https://substack.com/**
**Hashnode: https://hashnode.com/onboarding/new-story**""")
            print(f"  → Blogger 投稿成功")
            published += 1
        else:
            print(f"  → Blogger 投稿失敗: {result.error}")
            send_discord(f"❌ Blogger 投稿失敗\n{ja_article.title}")
            send_discord(f"""📝 Note用（日本語）
{ja_article.title}

**Note風（綺麗版）:** {storage['ja_formatted_url']}
**シンプルmd:** {storage['ja_simple_url']}

**ここから投稿してください:**
https://note.com/""")
            send_discord(f"""📝 Medium/Substack/Hashnode用（英語）
{en_article.title}

**Note風（綺麗版）:** {storage['en_formatted_url']}
**シンプルmd:** {storage['en_simple_url']}

**Medium: https://medium.com/new-story**
**Substack: https://substack.com/**
**Hashnode: https://hashnode.com/onboarding/new-story**""")

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
