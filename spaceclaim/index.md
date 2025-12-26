# ✏️ SpaceClaim スクリプト

SpaceClaim (Discovery) のモデリング操作を自動化するためのスクリプト群です。

## 🏗️ SpaceClaim API の基礎

SpaceClaim のスクリプトは、GUI 操作を Python コードとして記録・実行する形式が基本です。

### 1. オブジェクト階層
SpaceClaim のモデル構造は以下のようになっています。

- `Document`: 開いているドキュメント全体
- `Part`: コンポーネントやボディのコンテナ。`GetRootPart()` でトップレベルを取得。
- `DesignBody`: 3D ボディ（ソリッドやサーフェス）。
- `DesignFace` / `DesignEdge`: ボディを構成する面やエッジ。

### 2. 単位系と便利関数
SpaceClaim スクリプト内では、長さの内部単位は **メートル** です。
ミリメートルで値を指定したい場合は、`MM()` 関数を使用します。

```python
# 10.0 mm を指定する場合
length = MM(10.0) 
```

### 3. 選択と操作
```python
# ボディの全取得
root = GetRootPart()
bodies = root.Bodies

# 面の選択作成
selection = Selection.Create(bodies[0].Faces)

# 選択範囲に対してコマンドを実行（例：移動、色変更など）
# ...
```

## 📂 フォルダ構成

- **[modeling/](/spaceclaim/modeling/)**: 形状作成、クリーニング、修正など。
  - **[clean_geometry.py](https://github.com/your-org/ansys-scripting-cookbook/blob/main/spaceclaim/modeling/clean_geometry.py)**: 小さいエッジや面の削除、形状の簡略化。
- **[named-selection/](/spaceclaim/named-selection/)**: 面やボディの選択、Named Selection の作成。

## 🚀 実行方法

SpaceClaim 内の **Design (デザイン)** タブ -> **Script (スクリプト)** ボタンを押し、右側のエディタに貼り付けて実行してください。
詳細は [環境構築ガイド](/docs/setup) を参照してください。

## 💡 コツ: 「スクリプトの記録」を活用する
SpaceClaim のスクリプトエディタにある **Record (記録)** ボタンを押してから GUI 操作を行うと、対応する Python コードが自動生成されます。これをベースにループや条件分岐を追加するのが最も効率的な開発方法です。

