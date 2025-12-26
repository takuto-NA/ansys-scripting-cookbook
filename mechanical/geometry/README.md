# 🧊 Geometry Operations

Mechanical におけるジオメトリ操作（主にツリー上の操作や Named Selection の作成）に関するスクリプトです。

## 📖 解説: ジオメトリと名前付き選択

Mechanical 上でのジオメトリ操作は、主に「ボディの特定」と「Named Selection (名前付き選択) の作成」が中心となります。

```python
# Named Selection の新規作成
ns = Model.AddNamedSelection()
ns.Name = "MyNS"

# セレクションマネージャを使用してエンティティを割り当て
sel_mgr = ExtAPI.SelectionManager
ns.Location = sel_mgr.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
```

## 🛠️ スニペット一覧

- **[create_named_selection.py](./create_named_selection.py)**: ボディ名やキーワードに基づいて、Named Selection を自動作成します。

## 💡 主な用途

- 大規模モデルにおける境界条件設定の自動化。
- 特定の命名ルールに従ったボディのグループ化。
- メッシュ設定や結果評価のための部位特定。

