st='Sorting1234'
# s=[char for char in s]
f=list()
s=list()
o=list()
e=list()
for i in st:
    if i.isupper():
        s.append(i)
    elif i.islower():
        f.append(i)
    else:
        try:
            i=int(i)
            if i%2!=0:
                i=str(i)
                o.append(i)
            else:
                i=str(i)
                e.append(i)
        except:
            pass
r="".join(sorted(f))+"".join(sorted(s))+"".join(sorted(o))+"".join(sorted(e))
print(r)