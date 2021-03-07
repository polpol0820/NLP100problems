#10. 行数のカウント

"""
unixでの答え
wc -wl popular-names.txt
行数　単語数　バイト数が表示される

2780 11120  popular-names.txt

"""

"""
pandas
read_csv()：csvなどを読むやつ
read_table()：txt,可変長ファイルを読むやつ
"""
import pandas as pd

df = pd.read_table("./popular-names.txt",header = None,sep = "\t",names = ["name","sex","number","year"])
print("行数：",len(df))
print("単語数：",df.size)