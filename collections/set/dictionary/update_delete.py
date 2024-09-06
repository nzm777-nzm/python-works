
student={"name":"nzm","course":"datascience","place":"kerala"}

for i in student:
    
    if i == "course":
        
        student[i]="fullstack"

for i in student:
    
    if i == "place":
        
       new=student.pop(i)

print(new)
    
    
    
    