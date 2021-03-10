#zipfの法則

import MeCab
import japanize_matplotlib
import matplotlib.pyplot as plt
import collections
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


ans = []
for sentence in sentences:
    for morph in sentence:
        if morph["pos"] != "記号":
            ans.append(morph["base"])

ans = collections.Counter(ans)
cnt_ans = []
for key,val in ans.items():
    cnt_ans.append(val)
p = collections.Counter(cnt_ans)
x = []
for key,val in p.items():
    x.append(val)
rank = [r + 1 for r in range(len(x))]
plt.figure(figsize=(8, 4))
plt.scatter(rank,x)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('出現頻度順位')
plt.ylabel('出現頻度')
plt.show()
