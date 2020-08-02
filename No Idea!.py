l=input().split(" ")
inp=input().split()
hap=set(input().split())
sad=set(input().split())

map_inp=dict()

from collections import Counter
map_inp=Counter(inp)
inp=set(inp)

a=set(hap).intersection(inp)
b=set(sad).intersection(inp)

h=0
s=0

for i in a:
    h+=map_inp[i]
for i in b:
    s+=map_inp[i]

res=h-s

print(res)