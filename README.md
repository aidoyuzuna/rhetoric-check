# 論理チェックアプリ 🧠✨

ChatGPTとClaudeの両方を使って、文章の論理破綻・詭弁・認知の歪みを検出・分析するGUIアプリケーションです。

## 🎯 概要

このアプリケーションは、入力された文章に対してChatGPTとClaudeの2つのAIモデルから同時に分析結果を取得し、論理的な問題点を多角的に検証できます。

## ✨ 特徴

- **デュアルAI分析**: ChatGPT（GPT-5）とClaude（Sonnet 4）による並列分析
- **直感的なUI**: Fletを使用したモダンなデスクトップGUI
- **リアルタイム処理**: 送信ボタンクリック後、両AIから同時に回答を取得
- **キーボードショートカット対応**: 
  - `Ctrl + F`: 入力欄にフォーカス
  - `Ctrl + R`: 全フィールドをリセット
  - `Ctrl + Enter`: 分析を実行
- **音響フィードバック**: 分析完了時に効果音再生
- **ダークテーマ**: 目に優しい暗色系のUI

## 🛠️ 技術スタック

- **Python 3.x**
- **Flet**: クロスプラットフォーム GUI フレームワーク
- **OpenAI API**: ChatGPT統合
- **Anthropic API**: Claude統合
- **python-dotenv**: 環境変数管理

## 📋 必要な要件

```bash
flet
openai
anthropic
python-dotenv
```

## 🚀 セットアップ

### 1. リポジトリのクローン

```bash
git clone <repository-url>
cd rhetoric-check
```

### 2. 依存関係のインストール

```bash
# uvを使用する場合
uv install

# または pip を使用する場合
pip install flet openai anthropic python-dotenv
```

### 3. 環境変数の設定

プロジェクトルートに `.env` ファイルを作成し、APIキーを設定してください：

```env
OPENAI_KEY=your_openai_api_key_here
ANTHROPIC_KEY=your_anthropic_api_key_here
```

### 4. 音声ファイルの配置

`fin.wav` ファイルをプロジェクトルートに配置してください（分析完了時の効果音として使用）。

## 💻 使用方法

### アプリケーションの起動

```bash
python main.py
```

### 基本的な操作

1. **文章の入力**: 上部のテキストエリアに分析したい文章を入力
2. **分析の実行**: 「送信」ボタンをクリック、または `Ctrl + Enter`
3. **結果の確認**: 左側にChatGPTの分析結果、右側にClaudeの分析結果が表示
4. **リセット**: 「リセット」ボタンをクリック、または `Ctrl + R` で全フィールドをクリア

### キーボードショートカット

| ショートカット | 機能 |
|---------------|------|
| `Ctrl + F` | 入力欄にフォーカス |
| `Ctrl + R` | 全フィールドリセット |
| `Ctrl + Enter` | 分析実行 |

## 🏗️ アーキテクチャ

プロジェクトはMVCパターンに基づいて設計されています：

```
rhetoric-check/
├── main.py              # エントリーポイント・View層
├── app_controller.py    # Controller層（ビジネスロジック）
├── ai_service.py        # Model層（AIサービス統合）
├── components.py        # UIコンポーネント定義
├── fin.wav             # 効果音ファイル（要作成）
├── .env                # 環境変数（要作成）
└── README.md           # このファイル
```

### コンポーネント詳細

#### `main.py`
- アプリケーションのエントリーポイント
- UIレイアウトの定義
- Fletページの初期化

#### `app_controller.py`
- アプリケーションの状態管理
- ユーザーインタラクションの処理
- AI応答の調整・表示制御

#### `ai_service.py`
- OpenAI・Anthropic API統合
- 並列API呼び出し処理
- レスポンスの正規化

#### `components.py`
- 再利用可能なUIコンポーネント
- カスタムスタイリング
- `MyField`, `MyButton`, `AnswerField`クラス

## 🔍 分析対象

このアプリケーションは以下の論理的問題を検出・分析します：

- **論理破綻**: 前提と結論の間の論理的矛盾
- **詭弁**: 意図的に論理をすり替える議論手法
- **認知の歪み**: 認知バイアスによる思考の偏り

## 🚨 注意事項

- APIキーは必ず `.env` ファイルで管理し、バージョン管理には含めないでください
- API利用には料金が発生する場合があります
- インターネット接続が必要です