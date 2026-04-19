import os
import re
import shutil
import subprocess
from datetime import datetime
from pathlib import Path

ARTICLES_DIR = "articles"
GIT_REPO_URL = "https://github.com/jun915-a/content-auto"
RAW_BASE_URL = f"{GIT_REPO_URL}/raw/main"


def ensure_dir():
    """articles ディレクトリ作成"""
    Path(ARTICLES_DIR).mkdir(exist_ok=True)


def get_article_dir() -> tuple[str, str]:
    """記事用ディレクトリ（日付+時刻で一意性確保）"""
    timestamp = datetime.now().strftime("%Y-%m-%d-%H%M%S")
    date_dir = os.path.join(ARTICLES_DIR, timestamp)
    Path(date_dir).mkdir(parents=True, exist_ok=True)
    return date_dir, timestamp


def _sanitize_for_note(content: str) -> str:
    """Note 向け Markdown サニタイズ（Note は ##まで / テーブル・コードブロック非対応）"""
    # H3以降を H2 に統合
    content = re.sub(r"^#{3,}\s+", "## ", content, flags=re.MULTILINE)

    # コードブロックをプレーンテキスト化（``` を削除）
    content = re.sub(r"```[\w]*\n", "", content)
    content = content.replace("```", "")

    # テーブル行（| ... |）を箇条書きに変換
    lines = content.split("\n")
    new_lines = []
    for line in lines:
        stripped = line.strip()
        if re.match(r"^\|.*\|$", stripped):
            # セパレータ行（|---|---|）はスキップ
            if re.match(r"^\|[\s\-:|]+\|$", stripped):
                continue
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            cells = [c for c in cells if c]
            if cells:
                new_lines.append("- " + " / ".join(cells))
        else:
            new_lines.append(line)
    content = "\n".join(new_lines)

    # 連続する空行を1つに
    content = re.sub(r"\n{3,}", "\n\n", content)

    return content


def _format_note_style(title: str, content: str, language: str = "ja") -> str:
    """Note 用フォーマット（Note互換Markdownにサニタイズ）"""
    sanitized = _sanitize_for_note(content)
    if language == "ja":
        header = f"# {title}\n\n*ここに見出し画像を挿入*\n\n"
    else:
        header = f"# {title}\n\n*Insert header image here*\n\n"
    return header + sanitized


def save_article(ja_content: str, en_content: str, ja_title: str, en_title: str) -> dict:
    """4 つのファイル形式で記事を保存"""
    ensure_dir()
    date_dir, timestamp = get_article_dir()

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
    return {
        "ja_simple": ja_simple,
        "en_simple": en_simple,
        "ja_formatted": ja_formatted,
        "en_formatted": en_formatted,
        "ja_simple_url": f"{RAW_BASE_URL}/{ARTICLES_DIR}/{timestamp}/ja.md",
        "en_simple_url": f"{RAW_BASE_URL}/{ARTICLES_DIR}/{timestamp}/en.md",
        "ja_formatted_url": f"{RAW_BASE_URL}/{ARTICLES_DIR}/{timestamp}/ja_formatted.md",
        "en_formatted_url": f"{RAW_BASE_URL}/{ARTICLES_DIR}/{timestamp}/en_formatted.md",
        "timestamp": timestamp,
    }


def cleanup_old_articles(max_articles: int = 100):
    """100件以上になったら古いものから削除"""
    ensure_dir()

    dirs = []
    for item in os.listdir(ARTICLES_DIR):
        item_path = os.path.join(ARTICLES_DIR, item)
        if os.path.isdir(item_path):
            try:
                datetime.strptime(item, "%Y-%m-%d-%H%M%S")
                dirs.append((item, item_path))
            except ValueError:
                pass

    dirs.sort(reverse=True)  # 新しい順

    if len(dirs) > max_articles:
        to_delete = dirs[max_articles:]
        for timestamp, dir_path in to_delete:
            try:
                shutil.rmtree(dir_path)
                print(f"  [CLEANUP] {timestamp} を削除")
            except Exception as e:
                print(f"  [WARN] {timestamp} 削除失敗: {e}")


def commit_articles():
    """記事を git commit"""
    try:
        script = f"""
git config user.name "github-actions"
git config user.email "actions@github.com"
git add {ARTICLES_DIR}
git diff --staged --quiet || git commit -m "Add articles - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
"""
        result = subprocess.run(
            ["bash", "-c", script],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0 or "nothing to commit" in result.stderr:
            print("  [GIT] 記事を commit")
        else:
            print(f"  [GIT] commit 失敗: {result.stderr}")
    except Exception as e:
        print(f"  [GIT] エラー: {e}")
