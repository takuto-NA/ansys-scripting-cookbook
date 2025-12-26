# 📖 用語集

Ansys スクリプト開発でよく使われる用語と概念を説明します。

## 🔤 基本用語

### IronPython

**IronPython** は、.NET Framework 上で動作する Python の実装です。Ansys 製品（Mechanical, SpaceClaim など）の内部スクリプト環境では、**IronPython 2.7** が使用されています。

**特徴：**
- Python 2.7 の文法に準拠（Python 3.x とは異なる）
- `.NET` のクラスライブラリに直接アクセス可能
- `f-string` は使用不可（`.format()` を使用）

**関連ドキュメント：** [環境構築ガイド](./setup.md), [技術的な落とし穴](./reference/pitfalls.md)

### Journal (.wbjn)

**Journal** は、Ansys Workbench の操作を記録・再現するためのスクリプトファイルです。拡張子は `.wbjn` です。

**用途：**
- プロジェクトの保存・アーカイブ
- システムの追加・設定
- パラメータの一括更新

**関連ドキュメント：** [`workbench/`](../workbench/)

### Named Selection

**Named Selection（名前付き選択）** は、複数のジオメトリ要素（ボディ、面、エッジなど）をグループ化して名前を付けたものです。

**用途：**
- 境界条件の一括適用
- 結果の抽出範囲の指定
- 材料の割り当て

**例：**
```python
# Named Selection を作成
ns = Model.NamedSelections.AddNamedSelection()
ns.Name = "Fixed_Faces"
ns.Location = selected_faces
```

**関連ドキュメント：** [`mechanical/geometry/create_named_selection.py`](../mechanical/geometry/create_named_selection.py)

## 🏗️ Ansys の構造

### DataModel

**DataModel** は、Ansys Mechanical の内部データ構造へのアクセスを提供するオブジェクトです。スクリプト内でグローバル変数として自動的に利用可能です。

**主な用途：**
- 特定の型のオブジェクトを取得（`GetObjectsByType`）
- オブジェクトの検索

**例：**
```python
# 全ボディを取得
all_bodies = DataModel.GetObjectsByType(Ansys.ACT.Automation.Mechanical.Body)
```

### Model

**Model** は、Mechanical のツリー構造のルートに相当するオブジェクトです。ジオメトリ、境界条件、結果などにアクセスする際の起点となります。

**例：**
```python
# ジオメトリへのアクセス
geometry = Model.Geometry

# Named Selection の追加
ns = Model.NamedSelections.AddNamedSelection()
```

### Tree

**Tree** は、Mechanical のツリービュー（左側のパネル）に表示される階層構造を表します。スクリプトからは `Model` を通じてアクセスします。

## 🔧 開発関連

### Stub（スタブファイル）

**Stub** は、型情報のみを含む Python ファイルです。VS Code などの IDE で IntelliSense（入力補完）を有効にするために使用します。

**用途：**
- `DataModel`、`Model` などの Ansys API の型推論
- コード補完の向上

**関連ドキュメント：** [環境構築ガイド](./setup.md)

### IntelliSense

**IntelliSense** は、コードエディタが提供する入力補完機能です。変数名やメソッド名を入力すると、候補が自動的に表示されます。

**設定方法：** [環境構築ガイド](./setup.md)

## 📁 ファイル形式

### Parasolid (.x_t, .x_b)

**Parasolid** は、Ansys が推奨する中間フォーマットです。トポロジー情報が保持されやすく、自動化ワークフローに適しています。

**関連ドキュメント：** [CAD 互換性ガイド](./reference/cad-compatibility.md)

### STEP (.stp, .step)

**STEP** は、業界標準の3D CAD データ交換フォーマットです。色情報やレイヤー情報を保持できる場合があります。

**関連ドキュメント：** [CAD 互換性ガイド](./reference/cad-compatibility.md), [`interop/step-import-trick/`](../interop/step-import-trick/)

### SpaceClaim Document (.scdoc, .scdocx)

**SpaceClaim Document** は、Ansys SpaceClaim のネイティブ形式です。スクリプトとの親和性が最も高い形式です。

## 🔄 ワークフロー関連

### Plug-In モード

CAD ファイルを Workbench にアタッチする際のモードの一つ。CAD システムが起動している必要があります。

**関連ドキュメント：** [CAD 互換性ガイド](./reference/cad-compatibility.md)

### Reader モード

CAD ファイルを Workbench にアタッチする際のモードの一つ。CAD システムがインストールされている必要はありません。

**関連ドキュメント：** [CAD 互換性ガイド](./reference/cad-compatibility.md)

## 📊 解析関連

### Engineering Data

**Engineering Data** は、Workbench で材料の物性値を定義・管理するコンポーネントです。スクリプトから材料を割り当てる際は、ここに定義された材料名を使用します。

**関連ドキュメント：** [`mechanical/boundary-cond/batch_assign_materials.py`](../mechanical/boundary-cond/batch_assign_materials.py)

### Static Structural

**Static Structural** は、Ansys Workbench の解析システムの一つ。静的構造解析を実行します。

---

[← 戻る](../README.md) | [クイックスタートガイド →](./quickstart.md)

