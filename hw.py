'''
1.
cou=int(input('no of times u wantt to perform equations: '))
def add(x,y):
    c=x+y
    print(c)
def sub(x,y):
    c=x-y
    print(c)
def div(x,y):
    c=x//y
    print(c)
def mult(x,y):
    c=x*y
    print(c)
def power(x,y):
    c=x**y
    print(c)
print('for addition press 1','\n','for subtraction press 2','\n','for divison press 3','\n','for multition press 4','\n','for exponent press 5','\n')
for i in range(cou):
    a=int(input("first number: "))
    b=int(input("second number: "))
    k=int(input("which equation u want to do"))
    if k==1:
        add(a,b)
    if k==2:
        sub(a,b)
    if k==3:
        div(a,b)
    if k==4:
        mult(a,b)
    if k==5:
        power(a,b)

  
2.    
a=int(input('enter a number u want factorial for'))
c=1
for i in range(1,a+1):
    c*=i
print("factorial of ",a,"is",c)
hi.play()

3.
num = int(input("enter the number for fibonacci series")) 
n1, n2 = 0, 1 
print("Fibonacci Series:", n1, n2, end=" ") 
for i in range(2, num): 
    n3 = n1 + n2 
    n1 = n2 
    n2 = n3 
    print(n3, end=" ") 
print()

4.
cou=int(input('no of times u want to perform equations: '))
def circ(x):
    c=3.14*(x**2)
    print(c)
def rect(x,y):
    c=x*y
    print(c)
def tri(x,y):
    c=(x*y)/2
    print(c)
print('for area of circle press 1','\n','for area of rectangle press 2','\n','for area of triangle press 3')
for i in range(cou):
    k=int(input("which equation u want to do"))
    if k==1:
        r=int(input('enter radius'))
        circ(r)
    if k==2:
        a=int(input('enter length'))
        b=int(input('enter breadth'))
        rect(a,b)
    if k==3:
        a=int(input('enter height'))
        b=int(input('enter breadth'))
        div(a,b)

5.
l=[]
a=int(input('enter number of elements in list'))
for i in range(a):
    b=int(input("enter number"))
    l.append(b)
print('sum of list',l,'is',sum(l))

6.
for i in range(5,0,-1):
    print(i*'*')

7.
f=open(r'C:/Users/Admin/Desktop/hi.txt','r')
b=f.readlines()
for i in b:
    c=i.split()
for j in c:
    print(j,end='#')

8.
f=open(r'C:/Users/Admin/Desktop/hi.txt','r')
b=f.read()
vowel=0
const=0
up=0
lw=0
vow=['a','e','i','o','u','A','E','O','U','I']
for i in b:
    if i in vow:
        vowel+=1
    else:
        const+=1
    if i.islower()==True:
        up+=1
    else:
        lw+=1
print('no of vowels is',vowel)
print('no of consonants is',const)
print('no of uppercase letters is',up)
print('no of lowercase letters is',lw)

9.
f=open(r'C:/Users/Admin/Desktop/hi.txt','r')
b=f.readlines()
c=[]
for i in b:
    if 'a' in i:
        c.append(i)
f.close()
f=open(r'C:/Users/Admin/Desktop/lol.txt','w+')
for i in c:
    f.write(i)
f.close()

11.
f=open(r'C:/Users/Admin/Desktop/hi.txt','r')
try:
    while True:
        f.readline()
except EOFerror:
    f.close()
'''

import pickle
ch='y'
while ch=='y':
    l=[]
    roll=int(input("enter rollno"))
    try:
        exists=0
        f=open("C:\\Users\\AKSHARA\\Desktop\\Test1.dat","rb")
        while True:
            s=pickle.load(f)
            if s[0]==roll:
                print("roll number exists")
                exists=1
                break
            if exists==0:
                print("roll number doesn't exist")
                break
    except EOFError:
        f.close()

