group=input()
arr=input().split()
s=set()
s2=set()
for each in arr:
    if each not in s:
        s.add(each)
    else:
        s2.add(each)
        
print((s-s2).pop())