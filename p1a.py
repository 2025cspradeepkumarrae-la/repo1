name=input("Enter student name: ")
usn=input("Enter student usn: ")
marks1=int(input("Enter students marks1: "))
marks2=int(input("Enter students marks2: "))
marks3=int(input("Enter students marks3: "))
total_marks=marks1+marks2+marks3
per=total_marks/3
print('Student details')
print("name: ",name)
print('USN: ',usn)
print('Total marks obtained: ',total_marks)
print("Percentage is :",per)