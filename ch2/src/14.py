#14. 先頭からN行を出力

"""
head(n)で指定できる
"""
n = int(input())

import pandas as pd

df = pd.read_csv("./popular-names.txt",sep = "\t",names= ["name","sex","number","year"],header = None)
print(df.head(n))