#名詞の連接

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


#連接とは？？
#連続して出現する名詞
#最長一致で抽出(一番ながいもの)
ans = set()
for sentence in sentences:
    s = ""
    cnt = 0
    candidate = []
    index = []
    for morph in sentence:
        if morph["pos"] =="名詞":
            s += morph["surface"]
            cnt+=1
        else:
            candidate.append(s)
            index.append(cnt)
            s = ""
            cnt = 0
    if len(index)>0:
        max_index = max(index)
        for i in range(len(index)):
            if index[i] == max_index:
                found_index = i
                break
        ans.add(candidate[found_index])
for s in ans:
    print(s)