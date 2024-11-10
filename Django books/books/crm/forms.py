from django import forms

from crm.models import Books

from django.contrib.auth.models import User

class BookForm(forms.Form):
    
    name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    
    price=forms.IntegerField(widget=forms.TextInput(attrs={"class":"form-control"}))
    
    author=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    
    category=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    
    picture=forms.ImageField()
    
class BookUpdateForm(forms.ModelForm):
    
    class Meta:
        
        model=Books
        
        fields="__all__"
        
        widgets={
            
            "name":forms.TextInput(attrs={"class":"form-control"}),
            
            "author":forms.TextInput(attrs={"class":"form-control"}),
            
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            
            "category":forms.TextInput(attrs={"class":"form-control"}),
            
            "picture":forms.FileInput(attrs={"class":"form-control"})

        }
        
class SignupForm(forms.ModelForm):
    
    class  Meta:
        
        model=User
        
        fields=["username","email","password"]
        
class SignInForm(forms.Form):
    
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
        
        
        
        
        
        
        
    