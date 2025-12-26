# 🧊 Mechanical スクリプト (Python)

Ansys Mechanical (Simulation) の操作を自動化するためのスクリプト群です。

## フォルダ構成

- **[geometry/](./geometry/)**: ジオメトリの操作、Named Selection の作成など。
- **[boundary-cond/](./boundary-cond/)**: 境界条件の設定、材料の割り当て。
  - **[batch_assign_materials.py](./boundary-cond/batch_assign_materials.py)**: ボディ名に基づいた材料の一括割り当て。
- **[post-processing/](./post-processing/)**: 結果の抽出、レポート作成。
  - **[simple_export.py](./post-processing/simple_export.py)**: 最大応力値などのテキスト書き出し。

## 実行方法

Mechanical 内の **Automation (自動化)** タブ -> **Scripting (スクリプト)** ウィンドウにコードを貼り付けて実行してください。
詳細は [環境構築ガイド](../docs/setup.md) を参照してください。
