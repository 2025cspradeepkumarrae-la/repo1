import math
number =[]
num=int(input("How many numbers in the list :"))
for i in range(num):
    number.append(int(input("Enter the number :")))
print("The numbers in the list are :\n",number)
sum=0
for i in range(num):
    sum+=number[i]
print("sum is :",sum)
mean=sum/num
print("mean is :",mean)
sum1=0
for i in range(num):
    sum1+=math.pow((number[i]-mean),2)
v=sum1/num
print("varience is :",v)
sd=math.sqrt(v)
print("The standard deviation is:",sd)
             
