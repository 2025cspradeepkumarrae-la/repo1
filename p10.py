class student:
    def __init__(self,name="",usn=0,marks=0,total=0,per=0):
        self.name=name
        self.usn=usn
        self.marks=[]
        self.total=[]
        self.per=per
    def getMarks(self):
        for i in range(3):
            m=int(input("Enter the marks of student"+str(i+1)+":\n"))
            self.marks.append(m)
        total=sum(self.marks)
        self.total.append(total)
        self.per=(total/3)
    def display(self):
        print("Score card details:")
        print(self.name,'got',self.marks,'total is :',self.total,'percentage is',self.per)
name=input("Enter the name of student :\n")
usn=input("enter the usn of student:\n")
s1=student(name,usn)
s1.getMarks()
s1.display()