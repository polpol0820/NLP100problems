#11. タブをスペースに置換

"""
unixでの確認としてsed
sed -e "s/\t/ /g" ./popular-names.txt | head -n 5

"""

"""
pandasで空白に変換したものをans11.txtに保存している
"""
import pandas as pd

df = pd.read_table("./popular-names.txt",header=None,sep="\t")
df.to_csv("./ans11.txt",sep = " ",index = False,header = None)