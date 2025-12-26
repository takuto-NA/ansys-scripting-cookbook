# 📂 CAD 互換性と推奨フォーマット

Ansys で自動化ワークフローを構築する際、ジオメトリのインポート形式とバージョンの互換性は非常に重要です。

## 1. インポートモードの種類

Ansys Workbench では、CAD ファイルをアタッチする際に以下の 3 つのモードがあります。自動化を計画する際、対象の環境に CAD 本体がインストールされているかどうかが重要になります。

| モード | 内容 |
| :--- | :--- |
| **Plug-In モード** | CAD システムが起動している必要があります。 |
| **Reader モード** | CAD システムがインストールされている必要はありません。 |
| **Pseudo-Reader モード** | Ansys がバックグラウンドで CAD を起動し、アタッチ後に終了させます。 |

## 2. 推奨される中間フォーマット (2024 R2 時点)

自動化（特に SpaceClaim や Mechanical での操作）を前提とする場合、以下の順序で検討することを推奨します。

| フォーマット | 拡張子 | 推奨度 | 理由 |
| :--- | :--- | :--- | :--- |
| **Parasolid** | `.x_t`, `.x_b` | ⭐⭐⭐ | Workbench/Mechanical のカーネルに近く、トポロジーの欠落が少ない。色情報も保持。 |
| **STEP** | `.stp`, `.step` | ⭐⭐ | 業界標準。AP214/242 は色やレイヤー情報を保持可能。 |
| **SpaceClaim** | `.scdoc`, `.scdocx` | ⭐⭐⭐ | Ansys ネイティブ。自動化スクリプトとの親和性が最も高い。 |
| **IGES** | `.igs`, `.iges` | ⭐ | トポロジーが壊れやすく、自動化ワークフローでは非推奨。 |

## 3. サポートされている主なファイル形式

以下は Ansys 2024 R2 でサポートされている主なファイル形式と拡張子です。

- **ACIS**: `.sat`, `.sab`
- **AutoCAD**: `.dwg`, `.dxf`
- **Autodesk Inventor**: `.ipt`, `.iam`
- **CATIA**: `.CATPart`, `.CATProduct`, `.3dxml`, `.model`
- **Creo Parametric**: `.prt`, `.asm`
- **NX**: `.prt`
- **SOLIDWORKS**: `.sldprt`, `.sldasm`
- **Solid Edge**: `.par`, `.asm`, `.psm`
- **Fusion**: `.f3d`, `.f3z`
- **Rhinoceros**: `.3dm`

## 4. Ansys バージョン別 CAD サポート (目安)

一般的に、Ansys は最新の CAD バージョンを迅速にサポートしますが、スクリプトで自動処理する場合、CAD 側のバージョンを少し落とす（例：最新より 1 つ前）ことで安定性が増します。

| Ansys バージョン | 主要 CAD サポート状況 (例) |
| :--- | :--- |
| **2023 R2** | SolidWorks 2023, CATIA V5 R33, NX 2212 まで対応 |
| **2024 R1** | SolidWorks 2024, CATIA V5-6 R2023, NX 2306 まで対応 |
| **2024 R2** | SolidWorks 2024 (SP1+), CATIA V5-6 R2024, NX 2312 まで対応 |

> [!TIP]
> **SpaceClaim の活用**:
> スクリプトで形状修正を行う場合、SpaceClaim のネイティブ形式 (`.scdoc`) に一度変換して保存しておくと、後続の Mechanical 処理でのエラーを減らせます。

## 5. スクリプトでのインポートのコツ

- **パスの解決**: スクリプト内では絶対パスを使用するか、Workbench の `AbsUserPathName` を使用してパスを解決してください。
- **名前付き選択 (Named Selection)**: CAD 側で付けた名前を Mechanical に引き継ぐには、インポートオプションの `Named Selections` を `Yes` に設定する必要があります。

---
[← 戻る](../README.md)

