from tika import parser, initVM
import requests

# Javaサーバー初期化
initVM()

# Wordファイルをダウンロードして保存
url = 'https://file-examples.com/wp-content/uploads/2017/02/file-sample_100kB.docx'
file_path = 'sample.docx'
with open(file_path, 'wb') as f:
    f.write(requests.get(url).content)

# ファイルをTikaでパース
parsed = parser.from_file(file_path)

# タイトル（メタ情報）と本文表示
print("タイトル（metadata title）:", parsed['metadata'].get('title', 'なし'))
print("\n本文内容:\n", parsed['content'])
