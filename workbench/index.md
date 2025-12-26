# ⚙️ Workbench Journal (.wbjn)

Ansys Workbench のプロジェクト管理、システム構築、更新などを制御するジャーナルファイル群です。

## 🏗️ Workbench API の基礎

Workbench の操作は、IronPython 2.7 ベースの「ジャーナル」として記述されます。

### 1. グローバル関数
よく使用される主要な関数です。

| 関数 | 説明 |
| :--- | :--- |
| `GetProject()` | 現在のプロジェクトオブジェクトを取得します。 |
| `Save()` | プロジェクトを保存します。 |
| `GetSystem(Name="SYS")` | 特定の解析システム（例：Static Structural）を取得します。 |
| `UpdateAllDesignPoints()` | 全てのデザインポイント（パラメータセット）を更新します。 |

### 2. コンポーネントの操作と自動連携
```python
# システムの取得
system = GetSystem(Name="SYS")

# モデルコンポーネント (Mechanical) を取得
model = system.GetComponent(Name="Model")

# Mechanical を開く
model.Edit() # GUI を表示
# model.Edit(Interactive=False) # 非対話モード (バックグラウンド)

# Mechanical に Python スクリプトを送信して実行 (自動連携の核)
# これにより Workbench から Mechanical 内の操作を完全自動化できます
script = "Model.Mesh.GenerateMesh()"
model.SendCommand(Language='Python', Command=script)
```

## 📂 フォルダ構成

- **[basic-ops/](/workbench/basic-ops/)**: プロジェクトの保存、アーカイブ、コンポーネントの追加など。
- **[project-update/](/workbench/project-update/)**: プロジェクト全体の更新、パラメータセットの操作。
  - **[batch_run_csv.wbjn](https://github.com/your-org/ansys-scripting-cookbook/blob/main/workbench/project-update/batch_run_csv.wbjn)**: CSV ファイルからパラメータを読み込み、連続計算を実行。

## 🚀 実行方法

Workbench の **File** メニュー -> **Scripting** -> **Run Script File...** から、対象の `.wbjn` ファイルを選択してください。

## 💡 コメント
Workbench ジャーナルは GUI で行った操作の多くを記録できます (**File -> Scripting -> Record Journal...**)。複雑なシステム構築の自動化を行う際は、まず記録してコードの雛形を得るのが近道です。

