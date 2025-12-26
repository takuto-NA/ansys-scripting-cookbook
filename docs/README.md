# 📘 ドキュメント (Documentation)

Ansys スクリプト開発のための共通ガイド、環境構築、およびリファレンス資料です。

## 📖 このセクションについて

このディレクトリには、Ansys スクリプト開発に必要なすべてのドキュメントが含まれています。初心者向けのガイドから、上級者向けのリファレンスまで、段階的に学習できる構成になっています。

## 📚 ガイド

### 初心者向け

- **[🚀 クイックスタートガイド](./quickstart.md)**: 初めての方へ。5分で最初のスクリプトを実行できます。
- **[📖 用語集](./glossary.md)**: Ansys スクリプト開発でよく使われる用語を説明します。
- **[🔧 トラブルシューティングガイド](./troubleshooting.md)**: よくあるエラーとその解決方法。

### 環境構築

- **[🛠️ VS Code 環境構築ガイド](./setup.md)**: 入力補完（IntelliSense）の設定と実行方法。

## 📖 リファレンス

- **[📚 API 概要ガイド](./reference/api-overview.md)**: Mechanical / SpaceClaim / Workbench の API 構造と主要オブジェクト。
- **[📝 スクリプトテンプレート](./reference/script-template.md)**: 新規スクリプト作成時のテンプレートとコーディング規約。
- **[🐛 デバッグガイド](./reference/debugging.md)**: エラー発生時の調査方法とデバッグテクニック。
- **[⚠️ 技術的な落とし穴 (Pitfalls)](./reference/pitfalls.md)**: 日本語パス、単位系、パフォーマンス、外部ライブラリの制限など。
- **[📂 CAD 互換性ガイド](./reference/cad-compatibility.md)**: CAD ファイル形式の推奨事項と注意点。

## 🔍 逆引き

- **[🔍 チートシート](./cheatsheet.md)**: 「〇〇したい」から探せるコードスニペット集。

## 💡 開発のヒント

Ansys 内部の IronPython 2.7 は、通常の Python 3.x とは多くの点で挙動が異なります。

**初めての方は：**
1. **[クイックスタートガイド](./quickstart.md)** で最初のスクリプトを実行
2. **[用語集](./glossary.md)** で基本的な用語を理解
3. **[API 概要ガイド](./reference/api-overview.md)** で全体像を把握
4. **[環境構築ガイド](./setup.md)** で開発環境を整える

**スクリプトを書く時は：**
- **[チートシート](./cheatsheet.md)** でコードスニペットを探す
- **[スクリプトテンプレート](./reference/script-template.md)** で書き方を確認

**問題が発生したら：**
- **[デバッグガイド](./reference/debugging.md)** でエラー調査
- **[トラブルシューティングガイド](./troubleshooting.md)** でよくあるエラーを確認

---

[← 戻る](../README.md)
