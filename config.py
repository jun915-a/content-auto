import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
HF_API_TOKEN = os.environ.get("HF_API_TOKEN", "")
BLOGGER_API_KEY = os.environ.get("BLOGGER_API_KEY", "")
BLOGGER_BLOG_ID = os.environ.get("BLOGGER_BLOG_ID", "")
DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL", "")

# 生成記事数（1日あたり）
ARTICLES_PER_DAY = 3

# ニッチ（初期はテック/AI）
NICHE_KEYWORDS = ["AI", "machine learning", "LLM", "GPT", "Claude",
                  "tech", "programming", "startup", "software"]

# Redditサブレディット
REDDIT_SUBREDDITS = [
    "MachineLearning",
    "OpenAI",
    "LocalLLaMA",
    "artificial",
    "singularity",
    "programming",
]

# 記事フォーマット
ARTICLE_TEMPLATE = """
{summary}

---

## 詳細

{details}

---

*この記事は AI によって自動生成されました。*
"""
