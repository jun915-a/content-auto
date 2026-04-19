# content-auto 仕様書

## 概要

HackerNews / Reddit のトレンドを収集し、バズ度の高い記事を自動選定・生成して複数のブログプラットフォームに展開する自動コンテンツ生成システム。

GitHub Actions で4時間ごとに自動実行され、日本語・英語の両記事を同時生成する。

---

## システム全体フロー

```
[GitHub Actions (4時間ごと)]
        ↓
[トレンド収集]
 HackerNews (30件) + Reddit (30件, 任意)
        ↓
[バズ度スコアリング]
 スコア10点以上のみ通過 → 上位5件を選定
        ↓
[記事生成 (LLM 9段階フォールバック)]
 日本語版 + 英語版 を同時生成
        ↓
[自動投稿] Blogger (SendGrid 経由メール投稿)
        ↓
[GitHub 保存] 4形式のMarkdownファイル
        ↓
[Discord 通知] 手動投稿用URLを通知
        ↓
[手動投稿] Note / Medium / Substack / Hashnode
```

---

## 実行スケジュール

| 設定 | 値 |
|------|-----|
| 実行間隔 | 4時間ごと (`0 */4 * * *`) |
| 1回あたりの記事数 | 最大5件 |
| 1日の最大記事数 | 約30件 |

---

## トレンド収集

### ソース

| ソース | 取得数 | 備考 |
|--------|--------|------|
| HackerNews | 30件 | 常時有効 |
| Reddit | 30件 | GitHub Actions でブロックされる場合あり（オプション） |

**Reddit 対象サブレディット:**
- r/MachineLearning
- r/OpenAI
- r/LocalLLaMA
- r/artificial
- r/singularity
- r/programming

### バズ度スコアリング (`trend_ranker.py`)

トレンドをバズ度スコアで評価し、**10点以上のみ** 記事化対象にする。

**加点キーワード例（+3〜+25）:**
- 話題性: `breakthrough`, `revolutionary`, `game-changing`
- AI企業: `openai`, `anthropic`, `claude`, `nvidia`, `gpt-5/6`
- 感情喚起: `shocking`, `leaked`, `banned`, `mind-blowing`
- 発表系: `launches`, `unveils`, `reveals`
- 数値: 記事タイトル内の数字, `billion`, `record`

**減点キーワード例（-5〜-30）:**
- HN特殊投稿: `ask hn`, `who is hiring`
- 古い記事: `(1975)`, `archive`, `vintage`
- 教本系: `tutorial`, `introduction to`

**スコア補正:**
- タイトル長 40〜80文字: +8
- `?` 付き: +5
- 数字含む: +5
- 古い年号 `(19xx)`: -15

---

## 記事生成

### LLM フォールバックチェーン（9段階）

| 順番 | LLM | モデル | 特徴 |
|------|-----|--------|------|
| 1 | Groq | llama-3.3-70b-versatile | 高品質・高速（日次100k トークン） |
| 2 | Groq | llama-3.1-8b-instant | 70B の限界到達後の代替枠 |
| 3 | Gemini | gemini-2.5-flash | 広い無料枠 |
| 4 | Gemini | gemini-2.0-flash | 安定稼働 |
| 5 | Gemini | gemini-2.5-flash-lite | より高いレート |
| 6 | Mistral | mistral-small-latest | JSON mode 対応 |
| 7 | Mistral | ministral-8b-latest | Small の補助 |
| 8 | Together | Llama-3.3-70B-Instruct-Turbo-Free | 無料モデル |
| 9 | Cohere | command-r-08-2024 (v2 API) | 最終フォールバック |

**全 API で JSON mode / structured output を有効化** → パース失敗を大幅削減

### 生成される記事の構造

日本語版・英語版それぞれ同じ構造:

```
# [タイトル]

[冒頭要約 150-200文字]

---

## 📌 このトピックの本質
[200文字 コア解説]

## 🎯 5秒で分かるポイント
- ポイント1
- ポイント2
- ポイント3

## 📊 詳細解説
### 1. [要素1] (~150文字)
| 観点 | 説明 |
| --- | --- |
### 2. [要素2]
> 💡 Insight: [重要示唆]

## 🚀 実世界への影響
- 影響1
- 影響2

## ✨ 結論
[締めメッセージ]
```

---

## 保存・配信

### GitHub ファイル保存 (`article_storage.py`)

1記事あたり **4ファイル** を `articles/YYYY-MM-DD-HHMMSS/` に保存:

| ファイル | 内容 |
|----------|------|
| `ja.md` | 日本語シンプル版（タイトル + 本文） |
| `en.md` | 英語シンプル版 |
| `ja_formatted.md` | 日本語Note風（見出し画像プレースホルダー + 目次付き） |
| `en_formatted.md` | 英語Note風 |

**GitHub Raw URL 例:**
```
https://github.com/jun915-a/content-auto/raw/main/articles/2026-04-19-140530/ja_formatted.md
```

**自動クリーンアップ:** 100件を超えたら古い記事から順に削除

### 投稿先一覧

| プラットフォーム | 言語 | 投稿方法 |
|----------------|------|---------|
| Blogger | 日本語 | 自動（SendGrid メール投稿） |
| Note | 日本語 | 手動（Discord通知のURLからコピペ） |
| Medium | 英語 | 手動（Discord通知のURLからコピペ） |
| Substack | 英語 | 手動（Discord通知のURLからコピペ） |
| Hashnode | 英語 | 手動（Discord通知のURLからコピペ） |

### Discord 通知内容

記事1件につき最大4件の通知:
1. Blogger 投稿成功/失敗の通知
2. Note用 日本語URLセット
3. Medium/Substack/Hashnode用 英語URLセット
4. 実行完了サマリー（例: `📊 実行完了: 5/5件投稿`）

---

## 必要な環境変数 / Secrets

GitHub Actions の Secrets に以下を設定:

| 変数名 | 用途 | 必須 |
|--------|------|------|
| `GROQ_API_KEY` | Groq LLM | 推奨（1番目） |
| `GEMINI_API_KEY` | Gemini LLM | 推奨（3〜5番目） |
| `MISTRAL_API_KEY` | Mistral LLM | 推奨（6〜7番目） |
| `TOGETHER_API_KEY` | Together LLM | 任意 |
| `COHERE_API_KEY` | Cohere LLM | 任意 |
| `SENDGRID_API_KEY` | Blogger自動投稿 | Blogger利用時必須 |
| `SENDGRID_FROM_EMAIL` | SendGrid送信元アドレス | Blogger利用時必須 |
| `BLOGGER_BLOG_EMAIL` | Blogger受信メールアドレス | Blogger利用時必須 |
| `DISCORD_WEBHOOK_URL` | Discord通知 | 推奨 |

> 最低1つの LLM API キーが必要。`GROQ_API_KEY` + `GEMINI_API_KEY` の2つがあれば安定稼働。

---

## ファイル構成

```
content-auto/
├── main.py                  # エントリポイント・全体オーケストレーション
├── config.py                # 設定値・環境変数読み込み
├── trend_ranker.py          # バズ度スコアリング
├── tracker.py               # 投稿履歴管理（重複除外）
├── article_storage.py       # 記事のファイル保存・git commit
├── notifier.py              # Discord通知
├── requirements.txt         # 依存ライブラリ
├── sources/
│   ├── base.py              # TrendItem / TrendSource 基底クラス
│   ├── news.py              # HackerNews ソース
│   └── reddit.py            # Reddit ソース
├── generators/
│   └── article.py           # LLM 記事生成（9段階フォールバック）
├── publishers/
│   ├── base.py              # Publisher / PublishResult 基底クラス
│   └── blogger.py           # Blogger (SendGrid) 投稿
├── articles/                # 生成記事保存先（.gitignoreしない）
│   └── YYYY-MM-DD-HHMMSS/
│       ├── ja.md
│       ├── en.md
│       ├── ja_formatted.md
│       └── en_formatted.md
├── published_history.json   # 投稿履歴
└── .github/workflows/
    └── publish.yml          # GitHub Actions ワークフロー
```

---

## ローカル実行方法

```bash
# 1. 依存ライブラリのインストール
pip install -r requirements.txt

# 2. 環境変数の設定（.env ファイルを作成）
cp .env.example .env   # または手動で .env を作成
# .env に各 API キーを記入

# 3. 実行
python main.py
```

**.env ファイル例:**
```
GROQ_API_KEY=gsk_xxxx
GEMINI_API_KEY=AIzaSyxxx
MISTRAL_API_KEY=xxxx
SENDGRID_API_KEY=SG.xxxx
SENDGRID_FROM_EMAIL=your@gmail.com
BLOGGER_BLOG_EMAIL=xxxx@blogger.com
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/xxxx
```

---

## トラブルシューティング

| 症状 | 原因 | 対処 |
|------|------|------|
| `[LLM] 全て失敗` | APIクォータ枯渇 or 全API無効 | 翌日または複数APIキーを追加 |
| `429` エラー連発 | 1日のトークン制限超過 | 次の実行まで待機（4時間後） |
| `[GIT] commit 失敗` | git config 未設定 | article_storage.py の commit_articles が自動設定（修正済み） |
| Blogger に投稿されない | SendGridのFrom Email未認証 | SendGrid Sender Identity で `SENDGRID_FROM_EMAIL` を認証 |
| Reddit 403エラー | GitHub Actions からブロック | 正常動作（HackerNewsのみで継続） |
| 生成記事が0件 | バズ度フィルタで全除外 | min_score を下げる（trend_ranker.py の `min_score=10`） |

---

*最終更新: 2026-04-19*
