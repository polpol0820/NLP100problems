#13. col1.txtとcol2.txtをマージ
"""
pandas concatで結合
axis = 1で横方向に結合させている
"""
import pandas as pd

df1 = pd.read_csv("./col1.txt")
df2 = pd.read_csv("./col2.txt")
merge_1_2 =pd.concat([df1, df2],axis=1)
print(merge_1_2.head())
merge_1_2.to_csv("./ans13.txt",sep = "\t",index=False)