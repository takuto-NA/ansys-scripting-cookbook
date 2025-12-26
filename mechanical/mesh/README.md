# 🕸️ Mesh Operations

Mechanical におけるメッシュ制御（グローバル設定、ローカルサイズ指定）に関するスクリプトです。

## 📖 解説: メッシュ制御の API

Mechanical API では、`Model.Mesh` オブジェクトを介してメッシュ設定にアクセスします。

```python
# メッシュオブジェクトの取得
mesh = Model.Mesh

# グローバルサイズの変更
mesh.ElementSize = Quantity("10 [mm]")

# メッシュの生成
mesh.GenerateMesh()
```

## 🛠️ スニペット一覧

- **[set_global_mesh_size.py](./set_global_mesh_size.py)**: 全体のメッシュサイズを指定して生成します。
- **[add_local_sizing.py](./add_local_sizing.py)**: 特定の部位（Named Selection）に対してローカルサイズ設定（Sizing）を追加します。
- **[dynamic_face_sizing.py](./dynamic_face_sizing.py)**: 面の面積などの属性に基づいて動的に Named Selection を作成し、個別のサイズを適用します。

## 💡 主な用途

- 解析精度と計算コストのバランス調整の自動化。
- 特定の部位（フィレット部など）への細密メッシュの一括適用。
- パラメトリックスタディにおけるメッシュ解像度の動的変更。

