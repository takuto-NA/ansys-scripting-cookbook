---
layout: home

hero:
  name: "Ansys Scripting Cookbook"
  text: "実用的なスクリプトと開発ノウハウ"
  tagline: Ansys製品（Workbench, Mechanical, SpaceClaim）の自動化に必要な「実用的なスクリプト（レシピ）」と「開発ノウハウ」を集約
  actions:
    - theme: brand
      text: クイックスタート
      link: /docs/quickstart
    - theme: alt
      text: チートシート
      link: /docs/cheatsheet

features:
  - title: 🎯 実用的なコードスニペット
    details: コピー＆ペーストで即座に動くコードスニペットを提供します
  - title: 🛡️ 落とし穴の回避策
    details: IronPython (2.7) 特有の制限や落とし穴の回避策を解説します
  - title: 🌉 ツール間連携
    details: CAD → Workbench → Mechanical の連携テクニックを提供します
---

## 🌟 プロジェクト概要

このリポジトリは、Ansysの内部制御（IronPython/C#）をターゲットとした、コピー＆ペーストで即座に動くコードスニペットと、開発環境構築のベストプラクティスを提供します。

### 🎯 ターゲット

- 日々の解析業務を効率化したい現場のエンジニア
- 公式ヘルプの膨大な情報量に圧倒されているスクリプト初心者
- GUI操作の自動化（内部制御）を求めている層

### 💡 提供価値

- 実用的なコードスニペット
- IronPython (2.7) 特有の制限や落とし穴の回避策
- ツール間（CAD → Workbench → Mechanical）の連携テクニック

---

## 🗺️ ナビゲーションマップ

| カテゴリ | 内容 | リンク |
| :--- | :--- | :--- |
| **docs** | 📘 共通ガイド（クイックスタート、環境構築、用語集、トラブルシューティング） | [Link](/docs/) |
| **workbench** | ⚙️ Workbench Journal (.wbjn) | [Link](/workbench/) |
| **mechanical** | 🧊 Mechanical Scripting (Python) | [Link](/mechanical/) |
| **spaceclaim** | ✏️ SpaceClaim Scripting | [Link](/spaceclaim/) |
| **interop** | 🌉 ツール間連携 (The Bridge) | [Link](/interop/) |
| **common-snippets** | 💡 汎用ユーティリティ (Logging, File I/O) | [Link](/common-snippets/) |
| **examples** | 🚀 統合ワークフロー例 | [Link](/examples/) |

---

## 🚀 はじめに

**初めての方は、まず [クイックスタートガイド](/docs/quickstart) から始めてください。** 5分で最初のスクリプトを実行できます。

### 📚 学習パス

1. **[クイックスタートガイド](/docs/quickstart)**: 最初のスクリプトを実行してみる
2. **[用語集](/docs/glossary)**: Ansys 特有の用語を理解する
3. **[API 概要ガイド](/docs/reference/api-overview)**: API の構造と主要オブジェクトを把握する
4. **[環境構築ガイド](/docs/setup)**: VS CodeでIntelliSense（入力補完）を有効にする
5. **[チートシート](/docs/cheatsheet)**: 「〇〇したい」からコードを探す
6. **[トラブルシューティングガイド](/docs/troubleshooting)**: 問題が発生したら確認

### ❓ よくある質問

- **Q: Python の知識は必要ですか？**  
  A: 基本的な知識（変数、関数、ループなど）があると理解が早いですが、必須ではありません。スクリプトはコピー＆ペーストで動作します。

- **Q: どの Ansys バージョンで動作しますか？**  
  A: 各スクリプトの冒頭に動作確認バージョンが記載されています。一般的に 2023 R2 以降で動作します。

- **Q: エラーが発生したら？**  
  A: [トラブルシューティングガイド](/docs/troubleshooting) を確認してください。

---

## 🛠️ 技術ガイドライン

1. **言語仕様**:
   - 基本は **IronPython 2.7** 互換で記述（`f-string`禁止、`print()`関数の括弧使用推奨）。
   - 外部ライブラリ（NumPy, Pandas等）は原則使用禁止（標準環境で動作させるため）。
2. **動作確認バージョン**:
   - スクリプト冒頭に `# Tested on Ansys 2023 R2` のように確認済みバージョンを記載。
3. **モジュール性**:
   - 1つのスクリプトで何でもやろうとせず、機能ごとにファイルを分割。
4. **前提条件**:
   - スクリプト冒頭の Docstring に、必要な Named Selection や事前設定を明記。

---

## 🤝 コントリビューション

現在は初期構築フェーズです。バグ報告や機能リクエストは Issue で受け付けています。

---

## 📜 ライセンス

MIT License

