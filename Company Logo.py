from collections import Counter
s=input()
s=[char for char in s]
map_inp=dict(Counter(s))
map_inp={k: v for k, v in sorted(map_inp.items(), key=lambda item: item[1], reverse=True)}
di=dict()
for key in map_inp:
    if map_inp[key] not in di:
        l=list()
        l.append(key)
        di[map_inp[key]]=l
    else:
        l=di[map_inp[key]]
        l.append(key)
n=0
for key in di:
    li=di[key]
    li=sorted(li)
    for i in li:
        n+=1
        print("{} {}".format(i,key))
        if(n==3):
            break
    if(n==3):
        break