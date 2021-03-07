#17. １列目の文字列の異なり


import pandas as pd

df = pd.read_csv("./popular-names.txt",sep = "\t",names= ["name","sex","number","year"],header = None)

a = df["name"]
ans = set()
for item in a:
    ans.add(item)
print(len(ans))