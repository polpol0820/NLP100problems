#19 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる

import pandas as pd

df = pd.read_csv("./popular-names.txt",sep = "\t",names= ["name","sex","number","year"],header = None)

print(df["name"].value_counts())