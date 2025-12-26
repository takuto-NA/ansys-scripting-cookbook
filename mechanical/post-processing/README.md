# 📊 Post-Processing

解析結果の抽出、評価、および外部ファイルへのエクスポートに関するスクリプトです。

## 📖 解説: 結果の自動抽出

解析終了後、特定の結果（応力、変位、反力など）を取得し、CSVやテキストとして保存するワークフローを自動化できます。

```python
# 結果オブジェクトの取得
solution = Model.Analyses[0].Solution
stress = solution.AddEquivalentStress()

# 評価の実行
solution.EvaluateAllResults()

# 最大値の取得
max_stress = stress.Maximum.Value
```

## 🛠️ スニペット一覧

- **[simple_export.py](./simple_export.py)**: 最大応力値を取得し、テキストファイルにエクスポートします。
- **[export_cdb.py](./export_cdb.py)**: 解析モデル（メッシュ、境界条件等）を .cdb 形式でエクスポートします。

## 💡 主な用途

- 大量ケースの計算結果の自動集計。
- 特定の部位（Named Selection 等）における平均値・最大値の抽出。
- レポート作成の自動化。

