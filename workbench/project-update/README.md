# 🔄 Project Update & Parameters

Workbench プロジェクト全体の更新、およびパラメータセットの操作に関するジャーナルファイルです。

## 📖 解説: パラメータスタディの自動化

Workbench の「Parameter Set」をスクリプトから操作することで、多数のデザインポイントを効率的に処理できます。

```python
# パラメータの取得と変更
paramSet = GetProject().GetParameterSet()
param = paramSet.GetParameter(Name="P1")
param.Expression = "50 [mm]"

# 全体の更新
UpdateAllDesignPoints()
```

## 🛠️ スニペット一覧

- **[batch_run_csv.wbjn](./batch_run_csv.wbjn)**: CSV からパラメータを読み込み、連続計算を実行します。

## 💡 主な用途

- デザインポイント (Design Points) の一括更新。
- 外部ツール（最適化ツール等）からのパラメータ制御。
- 多数の形状案に対する一括解析。

