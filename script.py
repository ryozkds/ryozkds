import requests
import csv

# APIキー
API_KEY = 'YOUR_API_KEY'  # 取得したAPIキーをここに入力

# ユーザーからクエリを入力
query = input("検索クエリを入力してください: ")

# APIリクエストのURL
url = f'https://api.europeana.eu/record/v2/search.json?query={query}&rows=10&wskey={API_KEY}'

# APIリクエストの送信
response = requests.get(url)

if response.status_code == 200:  # 成功した場合
    data = response.json()
    items = data.get('items', [])
    
    # TSVファイルに書き込む
    with open('europeana_data.tsv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(['Title', 'Creator'])  # ヘッダー行

        for item in items:
            title = item.get('title', ['No Title'])[0]
            creator = item.get('dcCreator', ['Unknown'])[0]
            writer.writerow([title, creator])
    
    print("データを 'europeana_data.tsv' に保存しました。")
else:
    print(f"Error: {response.status_code}")
