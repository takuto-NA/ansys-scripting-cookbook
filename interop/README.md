# 🌉 ツール間連携 (Interop)

異なる Ansys 製品間、あるいは外部データと Ansys のやり取りを効率化するテクニックとスクリプトです。

## 📖 このセクションについて

このセクションでは、以下のような「ツール間の連携」を自動化するテクニックを提供します：

- **CAD → Ansys**: CAD ソフトウェア（Rhino など）で付けた色情報を Ansys の Named Selection に自動変換
- **Workbench → Mechanical**: Workbench のパラメータを Mechanical スクリプト内で活用
- **外部データ → Ansys**: CSV やテキストファイルからパラメータを読み込んで解析を自動化

これらのテクニックにより、GUI 操作を最小限に抑え、解析プロセスのボトルネックとなりやすい「ツール間のデータ受け渡し」を自動化できます。

## 📂 コンテンツ

- **[Color to Named Selection](./color_named_selection.md)**: STEP ファイルの色情報を Mechanical の Named Selection に自動変換する手法。
- **[Pass Parameters](./pass_parameters.md)**: Workbench のパラメータを Mechanical スクリプト内で活用する方法。

## 🔗 関連ドキュメント

- **[クイックスタートガイド](../docs/quickstart.md)**: 初めてのスクリプト実行
- **[用語集](../docs/glossary.md)**: Ansys スクリプト開発でよく使われる用語
- **[統合サンプル](../examples/README.md)**: エンドツーエンドのワークフロー例
- **[トラブルシューティング](../docs/troubleshooting.md)**: よくあるエラーと解決方法

---

[← 戻る](../README.md)
