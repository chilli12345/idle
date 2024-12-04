import mysql.connector as conec
con=conec.connect(host="localhost",user="root", password="2007", database="ip")
#refer for fetching
mycursor=con.cursor()


def read_lines(file_path, num_lines):
    lines = []
    with open(file_path, 'r') as file:
        for _ in range(num_lines):
            line = file.readline()
            if not line:
                break
            lines.append(line.strip())
    return lines


pre_teen=read_lines(r'C:\Users\Admin\Desktop\questions.txt',18)
teen=read_lines(r'C:\Users\Admin\Desktop\questions.txt',36)
y_adult=read_lines(r'C:\Users\Admin\Desktop\questions.txt',54)
adult=read_lines(r'C:\Users\Admin\Desktop\questions.txt',72)
o_adult=read_lines(r'C:\Users\Admin\Desktop\questions.txt',90)
old=read_lines(r'C:\Users\Admin\Desktop\questions.txt',108)

ans=[]#diff file

sol1=read_lines(r'C:\Users\Admin\Desktop\solutions.txt',3)
sol2=read_lines(r'C:\Users\Admin\Desktop\solutions.txt',21)
sol3=read_lines(r'C:\Users\Admin\Desktop\solutions.txt',42)

#introductions
print("Hi there! I hope you're doing okay.")
print("It's great that you're taking this step—it shows a lot of strength and self-awareness.")
print("Remember, this test is just a tool to help understand how you're feeling, and there's no judgment in whatever the results may be.")
print("Take your time, and know that support is always available.")

#input data of person
name=input('enter your name: ')
gender=input('enter your gender: ')
age=int(input('enter your age: '))

#
if age>=12 and age<=14:
    for i in range (4,len(pre_teen)):
        print(pre_teen[i])
        print("1:Never, 2:sometimes, 3:often, 4:always")
        ch=int(input('enter option: '))
        if ch>4 or ch<1:
            ch=int(input('enter correct option: '))
        ans.append(ch)
elif age>=15 and age<=17:
    for i in range (22,len(teen)):
        print(teen[i])
        print("1:Never, 2:Sometimes, 3:Often, 4:Always")
        ch=int(input('enter option: '))
        if ch>4 or ch<1:
            ch=int(input('enter correct option: '))
        ans.append(ch)
elif age>=18 and age<=26:
    for i in range (40,len(y_adult)):
        print(y_adult[i])
        print("1:Never, 2:Sometimes, 3:Often, 4:Always")
        ch=int(input('enter option: '))
        if ch>4 or ch<1:
            ch=int(input('enter correct option: '))
        ans.append(ch)
elif age>=27 and age<=36:
    for i in range (58,len(adult)):
        print(adult[i])
        print("1:Never, 2:Sometimes, 3:Often, 4:Always")
        ch=int(input('enter option: '))
        if ch>4 or ch<1:
            ch=int(input('enter correct option: '))
        ans.append(ch)
elif age>=37 and age<=45:
    for i in range (76,len(o_adult)):
        print(o_adult[i])
        print("1:Never, 2:Sometimes, 3:Often, 4:Always")
        ch=int(input('enter option: '))
        if ch>4 or ch<1:
            ch=int(input('enter correct option: '))
        ans.append(ch)
else:
    for i in range (93,len(old)):
        print(old[i])
        print("1:Never, 2:Sometimes, 3:Often, 4:Always")
        ch=int(input('enter option: '))
        if ch>4 or ch<1:
            ch=int(input('enter correct option: '))
        ans.append(ch)
slvl=sum(ans)
if slvl<=30:
    print('\n'+'\n')
    print("stress level: Normal")
    print('\n'+'\n')
    for i in range(len(sol1)):
                   print(sol1[i])
if slvl>=31 and slvl<=45:
    print('\n'+'\n')
    print("stress level: Elevated (Manageable)")
    print('\n'+'\n')
    for i in range(6,len(sol2)):
                   print(sol2[i])
if slvl>=46 and slvl<=60:
    print('\n'+'\n')
    print("stress level: High")
    print('\n'+'\n')
    for i in range(24,len(sol3)):
                   print(sol3[i])

