

class student:
    
    name:str
    
    age:int
    
    id:int
    
    gender:str
    
    course:str
    
    conatct:str
    
    address:str
    
    def __init__(self,id,age,gender,name,course,contact,address):
        
        self.id=id
        
        self.name=name
        
        self.gender=gender
        
        self.course=course
        
        self.contact=contact
        
        self.address=address
        
        self.age=age
        
    def display_student(self):
        
        print(self.id,self.name,self.address,self.contact,self.gender,self.age,self.course)

    def __str__(self):
        
        return self.name
        
#creating objects

student_instance=student(11,15,"male","nzm","python",9758587,"line 7")

# student_instance.display_student()

print(student_instance)