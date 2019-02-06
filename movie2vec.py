import MeCab
import gensim
import sys
import re
from gensim.models import word2vec

sys.path.append("/.pyenv/versions/anaconda3-4.3.1/envs/word2vec/lib/python3.6/site-packages")

#path = ["wakachi.txt"]
sentences = word2vec.LineSentence("wakachi.txt")

#model = gensim.models.Word2Vec.load('ja.bin')

model = word2vec.Word2Vec(sentences,
                          sg=1,
                          size=100,
                          min_count=1,
                          window=13,
                          hs=1,
                          negative=0)
while True:
    s = input()
    print(model.most_similar(s))

