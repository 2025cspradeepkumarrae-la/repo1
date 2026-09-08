def factorial(a):
    if a==1 or a==0:
        return 1
    else:
        return a * factorial(a-1)
def bino_coeff(n,r):
    b=(factorial(n))/(factorial(n-r)*factorial(r))
    return b
n=int(input("Enter the value of n: "))
r=int(input("Enter the value of r :"))
print("binomial coefficient is ",bino_coeff(n,r))