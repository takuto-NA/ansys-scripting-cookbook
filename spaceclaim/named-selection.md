# 🏷️ Named Selection (Groups)

SpaceClaim における Named Selection (Group) の作成と管理に関するスクリプトです。

## 📖 解説: Groups パネルとの関係

SpaceClaim 内で「Group」を作成すると、それが Mechanical へ渡された際に「Named Selection」として認識されます。

```python
# 選択範囲からグループを作成する基本コード
selection = Selection.Create(GetRootPart().Bodies[0])
NamedSelection.Create(selection, "MyNewGroup")
```

## 🛠️ スニペット例

具体的な作成例は、[Interop: Color to Named Selection](../interop/color_named_selection.md) 内の SpaceClaim スクリプトを参照してください。

## 💡 ヒント: 名前の重複
同じ名前のグループを `NamedSelection.Create` で作成しようとすると、エラーになるか、自動的に連番（`Group1`, `Group2`...）が振られる場合があります。作成前に既存のグループを確認することを推奨します。

---

[← 戻る](./README.md)

