# ⚡ Boundary Conditions

Mechanical における境界条件（荷重、拘束、接触、材料割り当て）の設定に関するスクリプトです。

## 📖 解説: 境界条件の操作

Mechanical API では、解析システム (`Analysis`) の下に境界条件がぶら下がっています。

```python
# 解析システムの取得
analysis = Model.Analyses[0]

# 荷重の追加例
force = analysis.AddForce()
force.Location = my_named_selection # Named Selection を割り当て
```

## 🛠️ スニペット一覧

- **[batch_assign_materials.py](./batch_assign_materials.py)**: ボディ名に含まれるキーワードに基づいて、材料を一括で割り当てます。

## 💡 主な用途

- 数百個の部品があるアセンブリへの材料設定の自動化。
- Named Selection を利用した荷重・拘束の一括適用。
- パラメトリックスタディにおける境界条件の動的変更。

