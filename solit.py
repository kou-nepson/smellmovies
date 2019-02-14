import os
import MeCab
import gensim
import sys
import re
from gensim.models import word2vec

sys.path.append("/.pyenv/versions/anaconda3-4.3.1/envs/word2vec/lib/python3.6/site-packages")
#dirname = os.path.dirname('/data/')
path = os.getcwd()
path += "/data"
#print(str(dirname))
files = os.listdir(path)
print(files)
files.pop(0) #.DS_Storeを削除
for i in files:
    with open("data/"+str(i)+"/newreview.txt","w") as n:
        with open("review.txt","rb") as f:
            binarydata = f.read()
            text = binarydata.decode('utf_8')
            text = re.sub(r'<br/>', '  ', text)
            text = re.sub(r'<br>', '  ', text)
            text = re.sub(r'</br>', '\n', text)
            text = re.sub(r'<div class="p-mark__review">', '\n', text)
            text = re.sub(r'</div>', '', text)
            text = re.sub(r'記録', '', text) #フィルマークスで記録とかくだけのレビューが大量にいるため
#        text = re.sub(r'[', '', text)
 #       text = re.sub(r']', '', text)
       # text = re.sub(r'<div id="kashi_area" itemprop="text">', '', text)
            n.write(text)
            print(i)

m = MeCab.Tagger("-Owakati")

for j in files:
    with open("data/"+str(j)+"/wakachi.txt","w") as f:
        text1 = text.splitlines() #テキストが多すぎるとNoneになるのでそれを回避する記述
        result = ""
        for t in text1:
            result += m.parse(t)
        print(j)
#        print(result)
        f.write(str(result)) # skip first \s
        with open("data/"+str(j)+"/wakachi.txt","rb") as f:
            allreview = ""
            allreview += str(f.read())
with open("wakachi.txt", "w") as f:
    f.write(allreview)

#print(result[0])

#sentences = word2vec.LineSentence("wakachi.txt")
#sentences = word2vec.Text8Corpus("wakachi.txt")
#model = word2vec.Word2Vec(sentences, size=100, window=5, min_count=5, workers=4)
#vector = model.wv["僕"]
#word = model.most_similar( [ vector ], [], 5)
#print(vector)
#print(word)

#model = word2vec.Word2Vec(sentences,
 #                         sg=1,
  #                        size=100,
   #                       min_count=1,
    #                      window=7,
     #                     hs=1,
      #                    negative=0)

#print(model.most_similar("が"))
