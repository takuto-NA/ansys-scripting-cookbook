# ⚙️ Basic Operations

Workbench プロジェクトの基本操作（保存、アーカイブ、システムの追加など）に関するジャーナルファイルです。

## 📖 解説: ファイル操作とシステム追加

Workbench では、プロジェクトファイル (`.wbpj`) の保存だけでなく、可搬性の高いアーカイブファイル (`.wbpz`) の作成も自動化できます。

```python
# アーカイブの作成例
Archive(FilePath="C:/Backup/Project.wbpz", IncludeItems=["Results", "ExternalFiles"])
```

## 🛠️ スニペット一覧

- **[save_and_archive.wbjn](https://github.com/your-org/ansys-scripting-cookbook/blob/main/workbench/save_and_archive.wbjn)**: 現在のプロジェクトを保存し、`.wbpz` 形式でアーカイブを作成します。

## 💡 主な用途

- 計算終了後の自動保存。
- バックアップ作成の自動化。
- 定型的な解析システムのテンプレート構築。

