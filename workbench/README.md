# ⚙️ Workbench Journal (.wbjn)

Ansys Workbench のプロジェクト管理、システム構築、更新などを制御するジャーナルファイル群です。

## フォルダ構成

- **[basic-ops/](./basic-ops/)**: プロジェクトの保存、アーカイブ、コンポーネントの追加など。
- **[project-update/](./project-update/)**: プロジェクト全体の更新、パラメータセットの操作。
  - **[batch_run_csv.wbjn](./project-update/batch_run_csv.wbjn)**: CSV ファイルからパラメータを読み込み、連続計算を実行。

## 実行方法

Workbench の **File** メニュー -> **Scripting** -> **Run Script File...** から、対象の `.wbjn` ファイルを選択してください。
