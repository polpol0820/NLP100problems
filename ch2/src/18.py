#18. 各行を3コラム目の数値の降順にソート

"""
ascending = 昇順
inplace = True 変数の中身を変更する（よくわからない）
"""

import pandas as pd

df = pd.read_csv("./popular-names.txt",sep = "\t",names= ["name","sex","number","year"],header = None)
df.sort_values(by = "number", ascending = False,inplace = True)
print(df.head())