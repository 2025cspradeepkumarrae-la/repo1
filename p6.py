import os 
infile=open("new.txt")
words=[]
for l in infile:
    temp=l.split()
    for i in temp:
        words.append(i)
infile.close()
print(words)
words.sort()
print("Sorted content:",words)
outfile=open("res.txt",'w')
for i in words:
    outfile.write(i)
    outfile.write(' ')
outfile.close()