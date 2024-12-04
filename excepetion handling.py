'''a=3
b=0
try:
    print(a/b)
except ZeroDivisionError:
    print("not divisible pls input another b values")
    b=int(input("enter b value"))
finally:
    print("done")
def a(p,q,t=2):
    return(p*t*q)/100
print(a(5,8,4))'''
def a(x):
    return x*x,x*x*x,x*x*x*x
b=3
x,y,z=a(b)
print(x,y)
