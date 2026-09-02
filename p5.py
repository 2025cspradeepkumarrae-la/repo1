import os,itertools
fname=input("Enter the file name:\n")
f1=open(fname)
d={}
for l in f1:
    words=l.split()
    for w in words:
        d.setdefault(w,0)
        d[w]+=1
print("Dictionary is",d)
v=list(d.values())
v.sort(reverse=True)
n={}
for i in v:
    for k in d:
        if d[k]==i:
            n.setdefault(k,i)
print("Reversed sorted list",n)
print(dict(itertools.islice(n.items(),3)))