
f=open("C:\\Users\\HP\\Desktop\\python_june_works\\file work\\students.txt","r")

students=[]

for stud in f:
    
    students.append(stud.rstrip("\n"))
    
print(students)