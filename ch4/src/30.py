#形態素解析結果の読み込み

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

for morph in sentences[2]:
    print(morph)