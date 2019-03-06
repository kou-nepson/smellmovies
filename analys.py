import os
import matplotlib.pyplot as plt
import sys
sys.path.append('.pyenv/versions/anaconda3-4.3.1/envs/py3.6.0/lib/python3.6/site-packages')
import numpy as np
from gensim.models import word2vec

model = word2vec.Word2Vec.load('models/learn.model')

path = os.getcwd()
path += "/data"
print("文章を入力してください")
data = "新鮮"
files = os.listdir(path)
print(files)
files.pop(0) #.DS_Storeを削除

values = [0,0,0,0,0,0]
for i in files:
    with open("data/"+str(i)+"/wakachi.txt", "rb") as f:
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
    count = 0
    print(i)
    print(new_id)
    for i in range(new_id):
        change = model.most_similar(data,[],new_id)[i][1]
        count += 1
        if change <= 0.5:
            break
    print(change)
    print(count)

def plot_polar(labels, values, imgname):
    angles = np.linspace(0, 2 * np.pi, len(labels) + 1, endpoint=True)
    values = np.concatenate((values, [values[0]]))  # 閉じた多角形にする
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    ax.plot(angles, values, 'o-')  # 外枠
    ax.fill(angles, values, alpha=0.25)  # 塗りつぶし
    ax.set_thetagrids(angles[:-1] * 180 / np.pi, labels)  # 軸ラベル
    ax.set_rlim(0 ,1000)
    fig.savefig(imgname)
    plt.close(fig)

labels = ['love', 'sin', 'impact', 'fresh','masterpiece','trend']
