from django import forms

class BmiForm(forms.Form):
    
    height=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-4 mt-2"}))
    
    weight=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-4 mt-2"}))
    
class BmrForm(forms.Form):
    
    height=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mt-2"}))
    
    weight=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mt-2"}))
    
    age=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mt-2"}))
    
    gender_choices=(
        ("male","male"),
        ("female","female")
    )
    
    gender=forms.ChoiceField(choices=gender_choices,widget=forms.Select(attrs={"class":"form-control form-select mt-2"}))
    
    activity_choices=(
        (1.2,"sedentary"),
        (1.375,"lightly active"),
        (1.55,"moderately active"),
        (1.725,"very active"),
        (1.9,"extra active")
    )
    
    activity=forms.ChoiceField(choices=activity_choices,widget=forms.Select(attrs={"class":"form-control form-select"}))
    
class EmiForm(forms.Form):
    
    loan_amount=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mt-2"}))
    
    intrest=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mt-2"}))
    
    tenure=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mt-2"}))
       
class GainorLossForm(BmrForm):
    
    mode_choices=(
        ("gain","gain"),
        ("loss","loss")
    )
    
    mode=forms.ChoiceField(choices=mode_choices)
    
    duration=forms.IntegerField()
    
    target_weight=forms.IntegerField()
     
class MilageForm(forms.Form):
    
    distance_travel=forms.IntegerField()
    
    fuel_consumed=forms.IntegerField()

class PercentageForm(forms.Form):
    
    amount=forms.IntegerField()
    
    percentage=forms.IntegerField()    

class ConversionForm(forms.Form):
    
    degree_celcius=forms.IntegerField()
    
    farehnheit=forms.IntegerField()
    
class LeapyearForm(forms.Form):
    
    year=forms.IntegerField()
    
class SignupForm(forms.Form):
    
    first_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    
    last_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    
    email_id=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    
class CustomerForm(forms.Form):
    
    first_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    
    last_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    
    address=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","rows":3}))
    
    pincode=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    
    city=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    
    state=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    
    postal=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    
    phone_number=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    
    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    
    about=(
        ("socialmedia","socialmedia"),
        ("friend","friend"),
        ("onsite","onsite")
    )
    
    about_us=forms.ChoiceField(choices=about,widget=forms.Select(attrs={"class":"form-control"}))
    
    specify=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    
    feedback=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","rows":3}))
    
    suggestion=forms.CharField(widget=forms.Textarea(attrs={"class":"form-comtrol","rows":3}))
    
    rec=(
        ("yes","yes"),
        ("no","no"),
        ("maybe","maybe")
    )
    
    recomended=forms.ChoiceField(choices=rec,widget=forms.RadioSelect)
    
    
    
       