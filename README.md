# 📘 ansys-scripting-cookbook

> Ansys製品（Workbench, Mechanical, SpaceClaim）の自動化に必要な「実用的なスクリプト（レシピ）」と「開発ノウハウ」を集約したリポジトリ。

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
| **docs** | 📘 共通ガイド（環境構築、IronPython基礎） | [Link](./docs/) |
| **workbench** | ⚙️ Workbench Journal (.wbjn) | [Link](./workbench/) |
| **mechanical** | 🧊 Mechanical Scripting (Python) | [Link](./mechanical/) |
| **spaceclaim** | ✏️ SpaceClaim Scripting | [Link](./spaceclaim/) |
| **interop** | 🌉 ツール間連携 (The Bridge) | [Link](./interop/) |
| **common-snippets** | 💡 汎用ユーティリティ (Logging, File I/O) | [Link](./common-snippets/) |
| **examples** | 🚀 統合ワークフロー例 | [Link](./examples/) |

---

## 🚀 はじめに

まずは **[環境構築ガイド](./docs/setup.md)** をご覧ください。VS CodeでIntelliSense（入力補完）を有効にする設定方法を解説しています。これが快適な開発の第一歩です。

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

