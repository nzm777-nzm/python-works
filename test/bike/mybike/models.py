from django.db import models



# Create your models here.

class BikeModel(models.Model):
    
    name=models.CharField(max_length=100)
    
    model=models.CharField(max_length=100)
    
    fuel_options=(
        ("petrol","petrol"),
        ("diesel","diesel"),
    )
    
    fuel_type=models.CharField(choices=fuel_options,default="petrol",max_length=100)
    
    picture=models.ImageField(upload_to="bike_images",blank=True,null=True)
    
    def __str__(self):
        
        return self.name
    
