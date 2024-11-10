from django.db import models

# Create your models here.

class Books(models.Model):
    
    name=models.CharField(max_length=100)
    
    price=models.PositiveIntegerField()
    
    author=models.CharField(max_length=100)
    
    category=models.CharField(max_length=100)
    
    picture=models.ImageField(upload_to="book_images",null=True)
    
    def __str__(self):
        
        return self.name
    
    
   
    

