num_of_words=int(input())
words=set()
seq=dict()
occ=dict()
for i in range(num_of_words):
    word=input()
    seq[word]=i
    if word not in words:
        words.add(word)
        occ[word]=1
    else:
        occ[word]+=1
print(len(seq))
for key in seq:
    print(occ[key], end=' ')