"""バズりそうなトレンドを厳選するスコアリング"""
import re
from typing import List


# バズ度を上げるキーワード（大文字小文字区別せず部分一致）
POSITIVE_KEYWORDS = {
    # 超話題性
    "breakthrough": 25, "revolutionary": 25, "world's first": 25,
    "first ever": 20, "game-changer": 20, "game changing": 20,
    "game-changing": 20, "disruptive": 18, "landmark": 15,

    # アクション動詞（発表系）
    "launches": 15, "launched": 15, "announces": 12, "unveils": 15,
    "releases": 10, "reveals": 12, "introduces": 10,
    "beats": 15, "surpasses": 15, "outperforms": 15,
    "dominates": 12, "crushes": 12,

    # AIホット企業
    "openai": 18, "anthropic": 18, "claude": 15, "gpt-5": 20,
    "gpt-6": 22, "gemini": 12, "deepseek": 12, "llama": 10,
    "nvidia": 15, "apple": 12, "tesla": 12, "google": 10,
    "microsoft": 10, "meta": 10, "mistral": 8,

    # AI/テック用語
    "agi": 22, "artificial general intelligence": 22,
    "llm": 10, "neural": 8, "transformer": 8,
    "agent": 12, "autonomous": 12, "reasoning": 10,
    "multimodal": 10, "vision": 8,

    # 感情系（クリックベイト要素）
    "shocking": 15, "shocked": 15, "stunning": 12,
    "incredible": 12, "amazing": 10, "mind-blowing": 18,
    "insane": 12, "wild": 10, "surprising": 12,
    "unbelievable": 12, "jaw-dropping": 15,

    # ネガティブ話題性（炎上/流出系）
    "banned": 18, "fired": 15, "leaked": 20, "exposed": 18,
    "lawsuit": 12, "sued": 12, "crisis": 10, "scandal": 15,
    "hack": 15, "hacked": 15, "vulnerability": 12, "breach": 12,
    "exploit": 12, "0-day": 15, "zero-day": 15,
    "fails": 10, "crashes": 10, "broken": 8,

    # 数字/記録系
    "billion": 12, "trillion": 15, "record": 12,
    "fastest": 10, "largest": 10, "smallest": 8,
    "cheapest": 10, "best ever": 12, "most powerful": 12,

    # 時事性
    "2026": 10, "just released": 15, "today": 5,
    "breaking": 15, "urgent": 12,

    # 興味喚起
    "why": 3, "how": 2, "what if": 8, "secret": 10,
    "hidden": 8, "untold": 10, "unknown": 5,

    # テック注目ワード
    "quantum": 12, "robotics": 10, "humanoid": 15,
    "self-driving": 12, "startup": 5, "ipo": 10,
    "acquisition": 12, "acquires": 10, "buys": 8,
}

# バズりにくいワード（減点）
NEGATIVE_KEYWORDS = {
    "ask hn": -25, "show hn": -15, "tell hn": -25,
    "who is hiring": -30, "who wants to be hired": -30,
    "freelancer": -20, "seeking freelancer": -25,

    # 歴史/古い記事
    "archive": -15, "history of": -10,
    "(1975)": -30, "(1980)": -25, "(1985)": -20,
    "(1990)": -15, "(1995)": -10, "(2000)": -8,
    "(2010)": -5, "(2015)": -3,
    "vintage": -15, "retro": -10, "classic": -5,

    # 教本/ドキュメント系
    "tutorial": -8, "introduction to": -5, "beginner": -5,
    "guide to": -3, "learn": -3,

    # 地域/ローカル系
    "local": -5, "small town": -10,

    # 技術が深すぎるニッチ
    "skiplist": -10, "ur-language": -10,
    "obscure": -8, "niche": -5,
}


def _clean_text(text: str) -> str:
    return (text or "").lower()


def score_virality(title: str, description: str = "", base_score: int = 0) -> int:
    """バズ度スコアを計算"""
    text = _clean_text(title) + " " + _clean_text(description)
    score = base_score

    # キーワードスコア
    for kw, pts in POSITIVE_KEYWORDS.items():
        if kw in text:
            score += pts

    for kw, pts in NEGATIVE_KEYWORDS.items():
        if kw in text:
            score += pts  # 負の値

    # タイトル長（バズりやすい 40-80 文字が理想）
    title_len = len(title)
    if 40 <= title_len <= 80:
        score += 8
    elif title_len < 25:
        score -= 10
    elif title_len > 120:
        score -= 5

    # 疑問符/感嘆符（引力）
    if "?" in title:
        score += 5
    if "!" in title:
        score += 3

    # 数字（具体性）
    if re.search(r"\d+", title):
        score += 5

    # 年号古い（古い記事ペナルティ）
    old_year = re.search(r"\((19\d{2}|20[01]\d)\)", title)
    if old_year:
        score -= 15

    return score


def rank_trends(trends: List, min_score: int = 10) -> List:
    """トレンドをバズ度でランク付け、閾値以下を除外"""
    scored = []
    for t in trends:
        virality = score_virality(t.title, t.description, t.score)
        t.virality_score = virality
        if virality >= min_score:
            scored.append(t)

    scored.sort(key=lambda x: x.virality_score, reverse=True)
    return scored
