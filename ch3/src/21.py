#21. カテゴリ名を含む行を抽出

import json 
import re

"""
reは正規表現
正規表現についてはもっと知る必要がありそう。。。
結構メンドクサイの塊
"""
json_open = open("./../jawiki-country.json","r")

for row in json_open:
    row = json.loads(row)
    if row["title"] == "イギリス":
        txt_uk = row["text"]
        break

pattern = r'^(.*\[\[Category:.*\]\].*)$'
result ='\n'.join(re.findall(pattern,txt_uk,re.MULTILINE))
print(result)