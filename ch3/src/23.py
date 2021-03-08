#23. セクション構造

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

pattern = r'^(\={2,})\s*(.+?)\s*(\={2,}).*$'
result ='\n'.join(i[1] + ":" + str(len(i[0])-1) for i in re.findall(pattern,txt_uk,re.MULTILINE))
print(result)