# Notion Paper Summarizer
## Overview
Notion上の論文DBに自動で要約を追加するためのスクリプト。現状はarxivのみ対応。

## Requirements
- Python
- Poetry

## Installation
1. 依存ライブラリのインストール
```
poetry install
```

2. `.env`にGemini APIキーを設定
```
GEMINI_API_KEY=gemini_api_key
```

## Usage
```
poetry run python src.main
```
