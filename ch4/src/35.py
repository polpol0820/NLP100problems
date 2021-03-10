#単語の出現頻度

import MeCab

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

word_list = []
for sentence in sentences:
    for morph in sentence:
        word_list.append(morph["base"])

import collections
word_list = collections.Counter(word_list)
ans = []
for key,val in word_list.items():
    ans.append([key,val])
ans = sorted(ans,key = lambda x: x[1],reverse=True)
for i in range(len(ans)):
    print(ans[i][0],ans[i][1])