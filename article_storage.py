import os
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Optional

ARTICLES_DIR = "articles"
GIT_REPO_URL = "https://github.com/jun915-a/content-auto"
RAW_BASE_URL = f"{GIT_REPO_URL}/raw/main"


def ensure_dir():
    """articles ディレクトリ作成"""
    Path(ARTICLES_DIR).mkdir(exist_ok=True)


def get_today_dir() -> str:
    """本日の記事ディレクトリ"""
    today = datetime.now().strftime("%Y-%m-%d")
    date_dir = os.path.join(ARTICLES_DIR, today)
    Path(date_dir).mkdir(parents=True, exist_ok=True)
    return date_dir


def _format_note_style(title: str, content: str, language: str = "ja") -> str:
    """Note 風のフォーマット（見出し、目次風）"""
    if language == "ja":
        header = f"# {title}\n\n[見出し画像]\n\n## 目次\n- このトピックの本質\n- 5秒で分かるポイント\n- 詳細解説\n- 影響・活用例\n- まとめ\n\n---\n\n"
    else:
        header = f"# {title}\n\n[Header Image]\n\nTable of Contents:\n- The Core\n- 5-Second Points\n- Detailed Breakdown\n- Impact & Use Cases\n- Conclusion\n\n---\n\n"
    return header + content


def save_article(ja_content: str, en_content: str, ja_title: str, en_title: str) -> dict:
    """4 つのファイル形式で記事を保存"""
    ensure_dir()
    date_dir = get_today_dir()

    # 1. シンプル md（タイトル + 内容）
    ja_simple = os.path.join(date_dir, "ja.md")
    en_simple = os.path.join(date_dir, "en.md")

    with open(ja_simple, "w", encoding="utf-8") as f:
        f.write(f"# {ja_title}\n\n{ja_content}")

    with open(en_simple, "w", encoding="utf-8") as f:
        f.write(f"# {en_title}\n\n{en_content}")

    # 2. Note 風フォーマット（見出し、目次付き）
    ja_formatted = os.path.join(date_dir, "ja_formatted.md")
    en_formatted = os.path.join(date_dir, "en_formatted.md")

    with open(ja_formatted, "w", encoding="utf-8") as f:
        f.write(_format_note_style(ja_title, ja_content, "ja"))

    with open(en_formatted, "w", encoding="utf-8") as f:
        f.write(_format_note_style(en_title, en_content, "en"))

    # GitHub Raw URL
    date_part = datetime.now().strftime("%Y-%m-%d")
    return {
        "ja_simple": ja_simple,
        "en_simple": en_simple,
        "ja_formatted": ja_formatted,
        "en_formatted": en_formatted,
        "ja_simple_url": f"{RAW_BASE_URL}/{ARTICLES_DIR}/{date_part}/ja.md",
        "en_simple_url": f"{RAW_BASE_URL}/{ARTICLES_DIR}/{date_part}/en.md",
        "ja_formatted_url": f"{RAW_BASE_URL}/{ARTICLES_DIR}/{date_part}/ja_formatted.md",
        "en_formatted_url": f"{RAW_BASE_URL}/{ARTICLES_DIR}/{date_part}/en_formatted.md",
        "date": date_part,
    }


def cleanup_old_articles(max_articles: int = 100):
    """100件以上になったら古いものから削除"""
    ensure_dir()

    dirs = []
    for item in os.listdir(ARTICLES_DIR):
        item_path = os.path.join(ARTICLES_DIR, item)
        if os.path.isdir(item_path):
            try:
                datetime.strptime(item, "%Y-%m-%d")
                dirs.append((item, item_path))
            except ValueError:
                pass

    dirs.sort(reverse=True)  # 新しい順

    if len(dirs) > max_articles:
        to_delete = dirs[max_articles:]
        for date_str, dir_path in to_delete:
            try:
                import shutil
                shutil.rmtree(dir_path)
                print(f"  [CLEANUP] {date_str} を削除")
            except Exception as e:
                print(f"  [WARN] {date_str} 削除失敗: {e}")


def commit_articles():
    """記事を git commit"""
    try:
        subprocess.run(
            ["git", "add", ARTICLES_DIR],
            check=True,
            capture_output=True,
        )
        result = subprocess.run(
            [
                "git",
                "commit",
                "-m",
                f"Add articles - {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            ],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            print("  [GIT] 記事を commit")
        else:
            print(f"  [GIT] commit 失敗: {result.stderr}")
    except Exception as e:
        print(f"  [GIT] エラー: {e}")
