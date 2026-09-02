num=int(input("Enter the length of fibonaccci sequence:\n"))
n1=0
n2=1
count=3
if num<=0:
    print("enter the number above zero")
elif num==1:
    print(n1)
elif num==2:
    print(n1)
    print(n2)
else :
    print(n1,end=" ")
    print(n2,end=" ")
    while(count<=num):
        n=n1+n2
        print(n,end=" ")
        n1=n2
        n2=n
        count+=1