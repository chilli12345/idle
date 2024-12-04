import pickle as p

with open('std.dat','wb') as f:
    l=['Emp_No','Emp_Name','Emp_Salary']
    l1=[1,'Aman',5000]
    l2=[2,'bipin',9000]
    l3=[3,'Amar',9900]
    p.dump(l,f)
    p.dump(l1,f)
    p.dump(l2,f)
    p.dump(l3,f)



f=open('std.dat','rb')
l=[]
try:
        while True:
            b=p.load(f)
            l.append(b)
except EOFError:
            print('eof')
print(l)
for i in l:
    if i.type()==int():
        
