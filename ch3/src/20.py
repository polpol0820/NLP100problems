#20. JSONデータの読み込み

import json 

json_open = open("./../jawiki-country.json","r")

for row in json_open:
    row = json.loads(row)
    if row["title"] == "イギリス":
        print(row["text"])
    
