# pdfread
練習用に作ってるものの仮置きです
# PDF Text Extractor with Apache Tika

任意のPDFファイルを読み込み、テキストデータとして抽出・保存するPythonスクリプトです。 
javaの導入が必要

## 🧰 使用ライブラリ

- [Apache Tika](https://github.com/chrismattmann/tika-python)
- requests
- 💡 注意事項
PDFによってはレイアウト崩れや空白行が多く出る場合があります

ファイル名に全角や特殊文字が入っている場合、パスの扱いに注意してください

テキスト抽出に時間がかかることがあります（Java側での処理のため）
