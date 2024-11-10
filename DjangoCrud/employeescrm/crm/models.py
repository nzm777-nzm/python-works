from django.db import models

# Create your models here. ok

class Employee(models.Model):
    
    name=models.CharField(max_length=100)
    
    age=models.PositiveIntegerField()
    
    gender=models.CharField(max_length=100)
    
    department=models.CharField(max_length=100)
    
    salary=models.PositiveIntegerField()
    
    address=models.TextField()
    
    qualification=models.CharField(max_length=100,null=True)
    
    mobile=models.PositiveBigIntegerField(null=True)
    
    def __str__(self):
        
        return self.name
    
    
