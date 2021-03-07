#16. ファイルをN分割する

"""
データをN等分するときはqcut()を使う
"""
n = int(input())

import pandas as pd
df = pd.read_csv("./popular-names.txt",sep = "\t",header = None,names = ["name","sex","number","year"])
def split_file(n):
    tmp = df.reset_index(drop=False)
    df_cut = pd.qcut(tmp.index,n,labels = [i for i in range(n)])
    df_cut = pd.concat([df,pd.Series(df_cut,name ="sp")],axis = 1)
    return df_cut

df_cut = split_file(n)
print(df_cut["sp"].value_counts())
print(df_cut.head())