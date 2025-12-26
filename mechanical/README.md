# 🧊 Mechanical スクリプト (Python)

Ansys Mechanical (Simulation) の操作を自動化するためのスクリプト群です。

## 🏗️ Mechanical API の基礎

Mechanical スクリプト（ACT）で最も頻繁に使用するグローバルオブジェクトです。

```mermaid
graph TD
    Global[グローバルオブジェクト] --> Model[Model<br/>モデルツリーのルート]
    Global --> DataModel[DataModel<br/>オブジェクト検索]
    Global --> ExtAPI[ExtAPI<br/>拡張API]
    Global --> Tree[Tree<br/>ツリービュー操作]
    
    Model --> Geometry[Geometry<br/>ジオメトリ]
    Model --> Analyses[Analyses<br/>解析システム]
    Model --> Mesh[Mesh<br/>メッシュ]
    
    DataModel --> GetObjectsByType[GetObjectsByType<br/>型で検索]
    DataModel --> GetObjectsByName[GetObjectsByName<br/>名前で検索]
    
    ExtAPI --> SelectionManager[SelectionManager<br/>選択マネージャ]
    
    style Global fill:#e1f5ff
    style Model fill:#fff4e1
    style DataModel fill:#e8f5e9
    style ExtAPI fill:#f3e5f5
```

| オブジェクト | 説明 |
| :--- | :--- |
| `Model` | モデルツリー全体のルート。`Model.Geometry` や `Model.Analyses` へアクセス。 |
| `DataModel` | オブジェクトの検索・管理。`DataModel.GetObjectsByType()` が強力。 |
| `ExtAPI` | 拡張 API。選択マネージャ (`SelectionManager`) や GUI 操作に使用。 |
| `Tree` | ツリービューの操作（フィルタリングや選択状態の変更など）。 |

## 💡 よく使うパターン

### 1. オブジェクトの検索
```python
# 全てのボディを取得
bodies = DataModel.GetObjectsByType(Ansys.ACT.Automation.Mechanical.Body)

# 名前でオブジェクトを検索
fixed_support = [obj for obj in DataModel.AllObjects if obj.Name == "Fixed Support"][0]
```

### 2. 単位を考慮した値の設定
```python
# Quantity クラスを使用して単位付きで設定
force.Magnitude.Output.SetData("100 [N]")
```

### 3. メッシュの生成と解析実行
```python
# メッシュ生成
Model.Mesh.GenerateMesh()

# 解析実行
Model.Analyses[0].Solve(True)
```

### 典型的なワークフロー

```mermaid
graph LR
    Start[スクリプト開始] --> GetGeo[ジオメトリ取得<br/>DataModel.GetObjectsByType]
    GetGeo --> CreateNS[Named Selection作成<br/>Model.AddNamedSelection]
    CreateNS --> SetMesh[メッシュ設定<br/>Model.Mesh.ElementSize]
    SetMesh --> GenerateMesh[メッシュ生成<br/>Model.Mesh.GenerateMesh]
    GenerateMesh --> SetBC[境界条件設定<br/>analysis.AddForce等]
    SetBC --> Solve[解析実行<br/>analysis.Solve]
    Solve --> GetResult[結果取得<br/>solution.AddEquivalentStress]
    GetResult --> Export[結果エクスポート<br/>analysis.ExportMechanicalData]
    Export --> End[完了]
    
    style Start fill:#e1f5ff
    style GetGeo fill:#fff4e1
    style CreateNS fill:#fff4e1
    style SetMesh fill:#e8f5e9
    style GenerateMesh fill:#e8f5e9
    style SetBC fill:#f3e5f5
    style Solve fill:#f3e5f5
    style GetResult fill:#c8e6c9
    style Export fill:#c8e6c9
    style End fill:#e1f5ff
```

## 📂 セクション

- **[ジオメトリ](./geometry.md)**: ジオメトリの操作、Named Selection の作成など。
- **[メッシュ](./mesh.md)**: メッシュサイズの設定、ローカルサイズコントロール。
- **[境界条件](./boundary-cond.md)**: 境界条件の設定、材料の割り当て。
  - **[batch_assign_materials.py](./batch_assign_materials.py)**: ボディ名に基づいた材料の一括割り当て。
- **[後処理](./post-processing.md)**: 結果の抽出、レポート作成。
  - **[simple_export.py](./simple_export.py)**: 最大応力値などのテキスト書き出し。

## 🚀 実行方法

Mechanical 内の **Automation (自動化)** タブ -> **Scripting (スクリプト)** ウィンドウにコードを貼り付けて実行してください。
詳細は [環境構築ガイド](../docs/setup.md) を参照してください。

## ⚠️ Tips
- **パフォーマンス**: 大規模モデルでは `DataModel.GetObjectsByType()` をループ内で多用せず、一度変数に格納してください。
- **APIリファレンス**: 詳細は [API 概要ガイド](../docs/reference/api-overview.md) を参照してください。

## 🔗 関連ドキュメント

- **[クイックスタートガイド](../docs/quickstart.md)**: 初めてのスクリプト実行
- **[用語集](../docs/glossary.md)**: Ansys スクリプト開発でよく使われる用語
- **[チートシート](../docs/cheatsheet.md)**: 「〇〇したい」からコードを探す
- **[トラブルシューティング](../docs/troubleshooting.md)**: よくあるエラーと解決方法

---

[← 戻る](../README.md)
