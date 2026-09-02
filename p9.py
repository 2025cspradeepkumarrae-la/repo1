class Complex:
    def initComplex(self):
        self.realpart=int(input("Enter the real part:"))
        self.imgpart=int(input("Enter the image part:"))
    def display(self):
        print(self.realpart,'+',self.imgpart,'i',sep=" ")
    def sum(self,c1,c2):
        self.realpart=c1.realpart+c2.realpart
        self.imgpart=c1.imgpart+c2.imgpart
c1=Complex()
c2=Complex()
c3=Complex()
print("Enter the first complex number:")
c1.initComplex()
print("first complex number:",end=" ")
c1.display()
print("Enter the Second complex number:")
c2.initComplex()
print("second complex number:",end=" ")
c2.display()
print("sum of the complex number is ",end=" ")
c3.sum(c1,c2)
c3.display()