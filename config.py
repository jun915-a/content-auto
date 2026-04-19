import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
MISTRAL_API_KEY = os.environ.get("MISTRAL_API_KEY", "")
TOGETHER_API_KEY = os.environ.get("TOGETHER_API_KEY", "")
COHERE_API_KEY = os.environ.get("COHERE_API_KEY", "")
SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "")
BLOGGER_BLOG_EMAIL = os.environ.get("BLOGGER_BLOG_EMAIL", "")
# 空文字列も fallback するため `or` を使用
SENDGRID_FROM_EMAIL = os.environ.get("SENDGRID_FROM_EMAIL") or "junconp419@gmail.com"
DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL", "")

# 生成記事数（1回の実行あたり）
ARTICLES_PER_DAY = 5

# Redditサブレディット
REDDIT_SUBREDDITS = [
    "MachineLearning",
    "OpenAI",
    "LocalLLaMA",
    "artificial",
    "singularity",
    "programming",
]

# 記事フォーマット（summary + details のみ、details内に既に見出しあり）
ARTICLE_TEMPLATE = """{summary}

{details}
"""
