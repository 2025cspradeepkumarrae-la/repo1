from datetime import date
name=input("Enter your name: ")
yearofbirth=int(input("Enter your birth year: "))
todaysdate=date.today()
currentyear=todaysdate.year
age=currentyear-yearofbirth
print("The age is : ",age)
if age>60:
    print("senior citizen")
else:
    print("not a senior citizen")    