#12. 1列目をcol1.txtに，2列目をcol2.txtに保存

import pandas as pd

df = pd.read_csv("./popular-names.txt",sep = "\t",header = None,names =["name","sex","number","year"])

col1 = df["name"]
col2 = df["sex"]
col1.to_csv("./col1.txt",index =False)
col2.to_csv("./col2.txt",index =False)

