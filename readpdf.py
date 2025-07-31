from tika import parser, initVM
import requests
import os

# JavaのTikaサーバー初期化（最初だけでOK）
initVM()

def parse_pdf_from_file(file_path):
    if not os.path.exists(file_path):
        print(f"ファイルが見つかりません: {file_path}")
        return
    parsed = parser.from_file(file_path)
    print(parsed['content'])

def parse_pdf_from_url(url):
    file_path = 'temp_downloaded.pdf'
    try:
        res = requests.get(url)
        res.raise_for_status()
        with open(file_path, 'wb') as f:
            f.write(res.content)
        print("PDFをダウンロードしました　解析します……")
        parse_pdf_from_file(file_path)
        os.remove(file_path)  # ダウンロード後は削除
    except requests.exceptions.RequestException as e:
        print(f"URL取得エラー: {e}")

# --- メイン処理 ---
mode = input("PDFを読み込む方法を選んでください（1: ローカルファイル, 2: URL）: ").strip()

if mode == '1':
    path = input("PDFファイルのパスを入力してください: ").strip()
    parse_pdf_from_file(path)

elif mode == '2':
    url = input("PDFのURLを入力してください: ").strip()
    parse_pdf_from_url(url)

else:
    print("不正な入力です")

