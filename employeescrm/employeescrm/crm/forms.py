from django import forms

from crm.models import Employee

from django.contrib.auth.models import User


class EmployeeForm(forms.ModelForm):
    
    class Meta:
        
        model=Employee
        
        fields="__all__"
        
        widgets={
            
            "name":forms.TextInput(attrs={"class":"form-control"}),
            
            "department":forms.TextInput(attrs={"class":"form-control"}),
            
            "salary":forms.NumberInput(attrs={"class":"form-control"}),
            
            "gender":forms.Select(attrs={"class":"form-control form-select"}),
            
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            
            "address":forms.Textarea(attrs={"class":"form-control","rows":5}),
            
            "date_of_join":forms.DateInput(attrs={"class":"form-control"}),
            
            "picture":forms.FileInput(attrs={"class":"form-control"})
        }
      
class SignupForm(forms.ModelForm):
    
    class  Meta:
        
        model=User
        
        fields=["username","email","password"]
        
        widgets={
            
            "username":forms.TextInput(attrs={"class":"form-control"}),
            
            "password":forms.TextInput(attrs={"class":"form-control"}),
            
            "email":forms.TextInput(attrs={"class":"form-control"})
        }
        
class SignInForm(forms.Form):
    
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))