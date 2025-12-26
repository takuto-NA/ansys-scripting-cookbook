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

### 2. コンポーネントの操作
```python
# システムの取得
system = GetSystem(Name="SYS")

# ジオメトリコンポーネントの編集（SpaceClaim/DesignModeler を起動）
geometry = system.GetComponent(Name="Geometry")
geometry.Edit()

# モデルコンポーネントの更新（Mechanical のデータ更新）
model = system.GetComponent(Name="Model")
model.Update()
```

## 📂 フォルダ構成

- **[basic-ops/](./basic-ops/)**: プロジェクトの保存、アーカイブ、コンポーネントの追加など。
- **[project-update/](./project-update/)**: プロジェクト全体の更新、パラメータセットの操作。
  - **[batch_run_csv.wbjn](./project-update/batch_run_csv.wbjn)**: CSV ファイルからパラメータを読み込み、連続計算を実行。

## 🚀 実行方法

Workbench の **File** メニュー -> **Scripting** -> **Run Script File...** から、対象の `.wbjn` ファイルを選択してください。

## 💡 コメント
Workbench ジャーナルは GUI で行った操作の多くを記録できます (**File -> Scripting -> Record Journal...**)。複雑なシステム構築の自動化を行う際は、まず記録してコードの雛形を得るのが近道です。
