import gensim
from gensim.models import word2vec
import sys
sys.path.append("/.pyenv/versions/anaconda3-4.3.1/envs/word2vec/lib/python3.6/site-packages")
import MeCab
import re

m = MeCab.Tagger("-Owakati")

with open("data/人間失格/ningen_shikkaku.txt","rb") as f:
    binarydata = f.read()
    text = binarydata.decode('shift_jis')

    # ルビ、注釈などの除去
    text = re.split(r'\-{5,}', text)[2]
    text = re.split(r'底本：', text)[0]
    text = re.sub(r'《.+?》', '', text)
    text = re.sub(r'［＃.+?］', '', text)
    text = text.strip()
#print(text[:200])


with open("data/人間失格/wakachi.txt","w") as f:
    result = m.parse(text)
    print(result[:200])
    f.write(result) # skip first \s
