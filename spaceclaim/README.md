# ✏️ SpaceClaim スクリプト

SpaceClaim (Discovery) のモデリング操作を自動化するためのスクリプト群です。

## フォルダ構成

- **[modeling/](./modeling/)**: 形状作成、クリーニング、修正など。
  - **[clean_geometry.py](./modeling/clean_geometry.py)**: 小さいエッジや面の削除、形状の簡略化。
- **[named-selection/](./named-selection/)**: 面やボディの選択、Named Selection の作成。

## 実行方法

SpaceClaim 内の **Design (デザイン)** タブ -> **Script (スクリプト)** ボタンを押し、右側のエディタに貼り付けて実行してください。
詳細は [環境構築ガイド](../docs/setup.md) を参照してください。
