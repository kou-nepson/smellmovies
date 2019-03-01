from gensim.models import word2vec

model = word2vec.Word2Vec.load('models/learn.model')
while True:
    s = input()
    print(model.most_similar(s))
