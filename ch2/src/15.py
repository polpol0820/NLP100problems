#15. 末尾からN行を出力

"""
tail(n)
"""
n = int(input())

import pandas as pd

df = pd.read_csv("./popular-names.txt",sep = "\t",names= ["name","sex","number","year"],header = None)
print(df.tail(n))