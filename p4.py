dic={}
c=input("Enter the multi-digit number :\n")
for i in c:
    dic.setdefault(i,0)
    dic[i]+=1
print("Frequency of each digit is : ")
print(dic)