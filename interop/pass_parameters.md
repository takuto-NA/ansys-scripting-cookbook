# 🌉 Workbench パラメータを Mechanical スクリプトで取得する

Workbench で定義した入力パラメータ（P1, P2 等）の値を、Mechanical 内部の Python スクリプトで取得し、解析制御に利用する方法を解説します。

## 1. 基本的な取得方法

Mechanical のスクリプト環境（Scripting コンソールや ACT）では、直接 Workbench のパラメータセットにアクセスする標準的なグローバル変数は提供されていません。

しかし、Mechanical のプロパティが「パラメータ化」されている場合、そのプロパティ値を参照することで間接的にパラメータ値を取得できます。

### 方法 A: 名前付き選択 (Named Selection) の詳細設定を利用する

最も確実な方法は、パラメータによって制御されているオブジェクトのプロパティを読み取ることです。

```python
# 例: 荷重値が Workbench パラメータ P1 で制御されている場合
force = DataModel.GetObjectsByName("MyForce")[0]
magnitude = force.Magnitude.Output.Value
print("Current Parameter Value: {}".format(magnitude))
```

## 2. ACT を利用した高度な連携

ACT (Ansys Customization Toolkit) を使用している場合は、XML 定義を介して Workbench パラメータと Mechanical の設定を直接紐付けることができます。

## 3. 回避策: ジャーナル経由での値渡し

Workbench Journal (`.wbjn`) から Mechanical スクリプトを実行する際、一時的なテキストファイルや環境変数を介して値を渡すことができます。

**Workbench Journal (`.wbjn`)**:
```python
# 値をファイルに書き出す
with open("C:/Temp/params.txt", "w") as f:
    f.write("100.0")

# Mechanical を実行
mechanical_system = GetSystem(Name="SYS")
mechanical_component = mechanical_system.GetComponent(Name="Model")
mechanical_component.Edit()
```

**Mechanical Script**:
```python
# ファイルから値を読み込む
with open("C:/Temp/params.txt", "r") as f:
    val = float(f.read())
# 解析設定に適用
Model.Analyses[0].AnalysisSettings.MaximumSubsteps = int(val)
```

## 4. まとめ

- Mechanical 内部からは Workbench 全体のパラメータセット (`GetProject().GetParameterSet()`) に直接アクセスできません。
- **「プロパティ経由の参照」** または **「外部ファイルを介した受け渡し」** が現実的な解決策となります。

---
[← 戻る](../README.md)

