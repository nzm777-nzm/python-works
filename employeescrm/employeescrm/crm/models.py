from django.db import models

# Create your models here.

class Employee(models.Model):
    
    name=models.CharField(max_length=100)
    
    department=models.CharField(max_length=100)
    
    salary=models.PositiveIntegerField()
    
    gender_option=(
        
        ("male","male"),
        ("female","female")
    )
    
    gender=models.CharField(max_length=100,choices=gender_option,default="male")
    
    email=models.EmailField(unique=True)
    
    address=models.TextField()
    
    date_of_join=models.DateField()
    
    picture=models.ImageField(upload_to="employee_images",null=True,blank=True)
    
    def __str__(self):
        
        return self.name
