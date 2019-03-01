# -*- coding:utf-8 -*-
import os
import matplotlib.pyplot as plt
import sys
sys.path.append('.pyenv/versions/anaconda3-4.3.1/envs/py3.6.0/lib/python3.6/site-packages')
from wordcloud import WordCloud
import numpy as np

#dirname = os.path.dirname('/data/')
path = os.getcwd()
path += "/data"
#print(str(dirname))
files = os.listdir(path)
print(files)
files.pop(0) #.DS_Storeを削除
allreview = ""
for i in files:
    with open("data/"+str(i)+"/wakachi.txt","rb") as f:
        binarydata = f.read()
        text = binarydata.decode('utf_8')
    wordcloud = WordCloud(background_color="white",
                      font_path="NotoSansCJKsc-Bold",
                      width=640,
                      height=480)
    # テキストからワードクラウドを生成する。
    wordcloud.generate(text)
    # ファイルに保存する。
    wordcloud.to_file('data/'+str(i)+'/wordcloud.png')
    # numpy 配列で取得する。
    img = wordcloud.to_array()
    print(i)  # (480, 640, 3)

with open("wakachi.txt","rb")as f:
    binarydata = f.read()
    text = binarydata.decode('utf-8')
wordcloud = WordCloud(background_color="white",
                  font_path="NotoSansCJKsc-Bold",
                  width=640,
                  height=480)
# テキストからワードクラウドを生成する。
wordcloud.generate(text)
# ファイルに保存する。
wordcloud.to_file('wordcloud.png')
# numpy 配列で取得する。
img = wordcloud.to_array()
print(img.shape)  # (480, 640, 3)
