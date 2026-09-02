def DivExp(a,b):
    assert a>0, ' a should be greater than zero'
    if b==0:
        raise Exception("Division by zero error")
    c=a/b
    return c
x=int(input('Enter the first number:\n'))

y=int(input('Enter the second number:\n'))
try :
    res=DivExp(x,y)
    print(res)
except Exception as err:
    print("An Expecton happened:"+str(err))