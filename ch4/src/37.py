#猫と共起の高いものを１０語

import MeCab
import japanize_matplotlib

txt_path = "./../neko.txt.mecab"
morphs = []
sentences = []
with open(txt_path,mode='r') as f:
    for line in f: #１行ずつ読み込む
        if line != 'EOS\n':
            fields = line.split("\t")
            if len(fields) != 2 or fields[0] == "": #空白と改行は無視
                continue
            else:
                attr = fields[1].split(",")
                morph = {"surface":fields[0],"base":attr[6],"pos":attr[0],"pos1":attr[1]}
                morphs.append(morph)
        else:
            sentences.append(morphs)
            morphs = []

#共起はよく一緒に出現する単語
#助詞とかを除いたほうがおもしろいかも

#まず猫が出現するものだけを取り出す
word_list = []
for sentence in sentences:
    if "猫" in [morph["base"] for morph in sentence]:
        for morph in sentence:
            if morph["pos"] == "記号" or morph["pos"] == "助詞" or morph["pos"] == "助動詞" or morph["base"] == "*\n":
                continue
            else:
                word_list.append(morph["base"])

import collections
word_list = collections.Counter(word_list)
ans = []
for key,val in word_list.items():
    if key != "猫":
        ans.append([key,val])
ans = sorted(ans,key = lambda x: x[1],reverse=True)
import matplotlib.pyplot as plt

X = []
Y = []
left = [i+1 for i in range(10)]
for i in range(10):
    X.append(ans[i][0])
    Y.append(ans[i][1])
plt.bar(left,Y,tick_label = X)
plt.grid(True)
plt.show()