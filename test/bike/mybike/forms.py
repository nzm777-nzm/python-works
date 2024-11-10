from django import forms

from mybike.models import BikeModel

class BikeForm(forms.ModelForm):
    
    class Meta:
        
        model=BikeModel
        
        fields="__all__"