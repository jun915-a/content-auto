import os
import json
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


def save_article(ja_content: str, en_content: str, ja_title: str, en_title: str) -> dict:
    """記事を保存して GitHub URL を返す"""
    ensure_dir()
    date_dir = get_today_dir()

    # 記事保存
    ja_file = os.path.join(date_dir, "ja.md")
    en_file = os.path.join(date_dir, "en.md")

    with open(ja_file, "w", encoding="utf-8") as f:
        f.write(f"# {ja_title}\n\n{ja_content}")

    with open(en_file, "w", encoding="utf-8") as f:
        f.write(f"# {en_title}\n\n{en_content}")

    # GitHub Raw URL
    date_part = datetime.now().strftime("%Y-%m-%d")
    ja_url = f"{RAW_BASE_URL}/{ARTICLES_DIR}/{date_part}/ja.md"
    en_url = f"{RAW_BASE_URL}/{ARTICLES_DIR}/{date_part}/en.md"

    return {
        "ja_file": ja_file,
        "en_file": en_file,
        "ja_url": ja_url,
        "en_url": en_url,
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
