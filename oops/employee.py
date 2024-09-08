
class person:
    
    eid:str
    
    age:int
    
    salay:int
    
    department:str
    
    
    def __init__(self,name,age,gender):
        
        self.name=name
        
        self.age=age
        
        self.gender=gender
        
    def display(self):
        
        print(self.name,self.age,self.gender)
        

class employee(person):
    
    
    def __init__(self,name,age,gender,eid,department,salary):
        
        
        super().__init__(name,age,gender)
        
        self.eid=eid
        
        self.department=department
        
        self.salary=salary
        
        # super().__init__(name,age,gender)
        
    def display(self):
        
        
        super().display()
        
        print(self.eid,self.department,self.salary)
        
emp_instance=employee("nzm",3,"male","e01","hr",100000)

emp_instance.display()


        
        