# 🌉 STEP の色・レイヤーによる Named Selection 自動化

CAD 側（CATIA, NX, SolidWorks 等）で部品や面に付けた「色」や「レイヤー」を Mechanical の Named Selection に自動変換するテクニックを解説します。

## 1. 2 つの実現方法

STEP ファイルの色やレイヤー情報を Named Selection (NS) に変換するには、以下の 2 つのアプローチがあります。

### A. 標準機能（インポート設定）を利用する方法
Mechanical のインポートオプションを設定するだけで、自動的に NS が作成されます。スクリプト不要で最も簡単な方法です。

### B. SpaceClaim スクリプトを利用する方法
より複雑な条件（例：特定の色かつ面積が一定以上など）で NS を作成したい場合に有効です。

---

## 2. 方法 A: 標準機能での設定 (Mechanical)

Workbench の Geometry コンポーネント、または Mechanical のインポート設定（Details view）で以下の項目を設定します。

| 設定項目 | 値 | 内容 |
| :--- | :--- | :--- |
| **Named Selections** | `Yes` | NS のインポートを有効化 |
| **Named Selections Key** | `Color` | 「色」をキーワードとして NS を作成 |

### 特定の色のみを抽出する場合
`Named Selections Key` に特定の値を指定することで、必要な色だけを NS 化できます。
- 例: `Color:255.0.0; Color:0.255.0` (赤と緑のみ)

### レイヤーを利用する場合
`Named Selections Key` に `Layer` を指定します。
- 例: `Layer:0; Layer:1`

---

## 3. 方法 B: SpaceClaim スクリプトでの実現

以下のスクリプトを SpaceClaim で実行すると、赤い面（RGB: 255, 0, 0）をすべて選択し、"NS_Load_Face" という名前の Named Selection を作成します。

```python
# SpaceClaim Script: Color to Named Selection
import SpaceClaim.Api.V19.Modeler as Modeler

def create_ns_by_color(r, g, b, ns_name):
    # すべての面を探索
    all_faces = GetRootPart().GetAllFaces()
    target_faces = []
    
    for face in all_faces:
        color = face.Color
        if color.R == r and color.G == g and color.B == b:
            target_faces.append(face)
            
    if target_faces:
        # 選択セットを作成
        selection = Selection.Create(target_faces)
        # Named Selection (Group) を作成
        NamedSelection.Create(selection, ns_name)
        print("Created NS: {} with {} faces".format(ns_name, len(target_faces)))

# RGB(255, 0, 0) = 赤色 の面を NS_Load_Face に変換
create_ns_by_color(255, 0, 0, "NS_Load_Face")
```

## 4. Mechanical 側での利用

上記で作成された "NS_Load_Face" は、Mechanical にインポートした際に自動的に Named Selection として認識されます。
これを利用して、Mechanical スクリプト側で荷重を割り当てることができます。

```python
# Mechanical Script
ns = DataModel.GetObjectsByName("NS_Load_Face")[0]
force = Model.Analyses[0].AddForce()
force.Location = ns
```

## 5. ベストプラクティス

- **CAD 側での運用ルール**: 「固定面は青(0,0,255)」「荷重面は赤(255,0,0)」のように色と意味を標準化しておくと、完全自動解析が実現します。
- **Parasolid の利用**: STEP よりも Parasolid (`.x_t`) の方が色が安定して保持される場合があります。

---
[← 戻る](../README.md)

