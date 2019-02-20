# -*- coding:utf-8 -*-
import os
import sys
import gensim
import numpy as np
from gensim.models import word2vec
import gensim.downloader as api
from gensim.models.keyedvectors import KeyedVectors

#word_vectors = api.load("glove-wiki-gigaword-100")
sys.path.append("/.pyenv/versions/anaconda3-4.3.1/envs/word2vec/lib/python3.6/site-packages")

path = os.getcwd()
path += "/data"
#print(str(dirname))
files = os.listdir(path)
print(files)
files.pop(0) #.DS_Storeを削除
for fnum in files:
    print(fnum)
    sentences = word2vec.LineSentence("data/"+str(fnum)+"/wakachi.txt")

    sentences = gensim.models.word2vec.Text8Corpus("data/"+str(fnum)+"/wakachi.txt")
    model = word2vec.Word2Vec(sentences, size=100, window=5, min_count=5, workers=4)
#vector = model.wv["新鮮"]
#word = model.most_similar( [ vector ], [], 100)
#print(vector)
#print(word)
#while hoge >= 0.6:
#    i = 1
#    hoge = model.most_similar( [ vector ], [], i)
#    i += 1
#    print(i)
    with open("data/"+str(fnum)+"/wakachi.txt", "rb") as f:
        binarydata = f.read()
        text = binarydata.decode('utf_8')
    words = text.split(' ')
    word_to_id = {}
    id_to_word = {}
    for word in words:
        if word not in word_to_id:
            new_id = len(word_to_id)
            word_to_id[word] = new_id
            id_to_word[new_id] = word
    print(new_id)
#print(id_to_word[3])
    count = 0
    sim_count = 0
    print("キーワードを入力してください")
    keyword = input()
    for i in word_to_id:
        distance = model.wmdistance(keyword, i)
        if distance <= 6.0:
            sim_count += 1
        #print(sim_count)
        #print(count)
        count += 1
    print(sim_count)
    #kj    print("{:.5f}".format(distance))
    percent = sim_count / new_id
    print(percent)
    with open("data/"+str(fnum)+"/identity.txt","w")as f:
        f.write("全単語")
        f.write(str(new_id)+"\n")
        f.write("のうち")
        f.write(keyword)
        f.write("の近くの単語は")
        f.write(str(sim_count)+"\n")
        f.write("割合は")
        f.write(str(percent)+"\n")

