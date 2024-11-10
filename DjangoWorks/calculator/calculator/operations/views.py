from django.shortcuts import render

from django.views.generic import View,TemplateView

from operations.forms import BmiForm,BmrForm,EmiForm,GainorLossForm,MilageForm,PercentageForm,ConversionForm,LeapyearForm,SignupForm,CustomerForm

class AdditionView(View):
    
    template_name="addition.html"
    
    def get(self,request,*args,**kwargs):
        
        return render(request,self.template_name)
    
    def post(self,request,*args,**kwargs):
        
        n1=request.POST.get("num1")
        
        n2=request.POST.get("num2")
        
        result=int(n1)+int(n2)
        
        return render(request,self.template_name,{"result":result})
    
class SubtactionView(View):
    
    template_name="sub.html"
    
    def get(self,request,*args,**kwargs):
        
        return render(request,self.template_name)
    
    def post(self,request,*args,**kwargs):
        
        n1=request.POST.get("num1")
        
        n2=request.POST.get("num2")
        
        result=int(n1)-int(n2)
        
        return render(request,self.template_name,{"result":result})

class MultiplicationView(View):
    
    template_name="multi.html"
    
    def get(self,request,*args,**kwars):
        
        return render(request,self.template_name)
    
    def post(self,request,*args,**kwargs):
        
        n1=request.POST.get("num1")
        
        n2=request.POST.get("num2")
        
        result=int(n1)*int(n2)
        
        return render(request,self.template_name,{"result":result})
        
class DivisionView(View):
    
    template_name="div.html"
    
    def get(self,request,*args,**kwargs):
        
        return render(request,self.template_name)
    
    def post(self,request,*args,**kwargs):
        
        n1=request.POST.get("num1")
        
        n2=request.POST.get("num2")
        
        result=int(n1)/int(n2)
        
        return render(request,self.template_name,{"result":result})
    
class CubeView(View):
    
    template_name="cube.html"
    
    def get(self,request,*args,**kwargs):
        
        return render(request,self.template_name)
    
    def post(self,request,*args,**kwargs):
        
        n1=request.POST.get("num1")
        
        result=int(n1)**3
        
        return render(request,self.template_name,{"result":result})
        
class FactorialView(View):
    
    template_name="fact.html"
    
    def get(self,request,*args,**kwargs):
        
        return render(request,self.template_name)
    
    def post(self,request,*args,**kwargs):
        
        n1=request.POST.get("num1")
        
        fact=int(1)
        
        for i in range(int(1),int(n1)+int(1)):
            
            fact=fact*i
            
        result=(f"{n1}!={fact}")
        
        # return render(request,self.template_name,{"factorial":result})
        
        # return render(request,self.template_name,{"factorial":n1})
        
        return render(request,self.template_name,{"factorial":result})
       
class BmiView(View):
    
    template_name="bmi.html"
    
    def get(self,request,*args,**kwargs):
        
        
        form_instance=BmiForm()
        
        
        return render(request,self.template_name,{"form":form_instance})
    
    
    def post(self,request,*args,**kwargs):
        
        
          #step 1 extract form data
       
       form_data=request.POST
       
       #initialize form instance with form data
       
       form_instance=BmiForm(form_data)
       
       #step3 check valid
       
       if form_instance.is_valid():
           
          height=form_instance.cleaned_data.get("height")
          
          weight=form_instance.cleaned_data.get("weight")
          
          bmi=weight/(height/100)**2
       
       return render(request,self.template_name,{"form":form_instance,"result":bmi})
   
def calculate_bmr(height,weight,age,gender):
    
    if gender=="male":
        
        bmr=10*weight+6.25*height-5*age+5
        
    else:
        
        bmr=10*weight+6.25*height-5*age-161
        
    return bmr
        
def dail_calory(bmr,activity):
    
    return float(activity)*bmr
   
class BmrView(View):
    
    template_name="bmr.html"
    
    def get(self,request,*args,**kwargs):
        
        form_instance=BmrForm
        
        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        
        form_data=request.POST
        
        form_instance=BmrForm(form_data)
        
        if form_instance.is_valid():
            
            data=form_instance.cleaned_data
            
            height=data.get("height")
            
            weight=data.get("weight")
            
            age=data.get("age")
            
            gender=data.get("gender")
            
            activity=data.get("activity")
            
            bmr=calculate_bmr(height,weight,age,gender)
            
            print(height,weight,age,gender,activity)
            
            calorie=dail_calory(bmr,activity)
            
            print(calorie)
                 
        return render(request,self.template_name,{"form":form_instance,"result":calorie})
    
class EmiView(View):
    
    template_name="emi.html"
    
    def get(self,request,*args,**kwargs):
        
        form_instance=EmiForm
        
        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        
        from_data=request.POST
        
        form_instance=EmiForm(from_data)
        
        if form_instance.is_valid():
            
            loan_amount=form_instance.cleaned_data.get("loan_amount")
            
            intrest=form_instance.cleaned_data.get("intrest")
            
            intrest=intrest/(12*100)
            
            tenure=form_instance.cleaned_data.get("tenure")
            
            emi=emi=loan_amount*intrest*((1+ intrest)**tenure) / ((1+intrest)**tenure -1)
            
            total_intrest=form_instance.cleaned_data.get("total_intrest")
            
            total_intrest=tenure*emi
            
            total_amount=total_intrest*tenure
            
        return render(request,self.template_name,{"form":form_instance,"result":emi,"totalin":total_intrest,"total":total_amount})
    
class GainorlossView(View):
    
    template_name="gainorloss.html"
    
    form_class=GainorLossForm
    
    def get(self,request,*args,**kwargs):
        
        form_instance=self.form_class
        
        return render(request,self.template_name,{"form":form_instance})
    
    
    def post(self,request,*args,**kwargs):
        
        form_data=request.POST
        
        form_instance=GainorLossForm(form_data)
        
        if form_instance.is_valid():
            
            data=form_instance.cleaned_data
            
            height=data.get("height")
            
            weight=data.get("weight")
            
            age=data.get("age")
            
            gender=data.get("gender")
            
            activity=data.get("activity")
            
            mode=data.get("mode")
            
            duration=data.get("duration")
            
            target_weight=data.get("target_weight")
            
            print(height,weight,age,gender,activity,mode,duration,target_weight)
            
            bmr=calculate_bmr(height,weight,age,gender)
            
            calories=dail_calory(bmr,activity)
            
            target_calories=target_weight*7700
            
            days=duration*7
            
            daily_target_calories=target_calories/days
            
            total_calories=0
            
            if mode=="gain":
                
                total_calories=calories+daily_target_calories
                
            else:
                
                total_calories=calories-daily_target_calories
                
            # print("calorie to maintain current weight",calories)
            
            # print(f"total daily calories to {mode} {target_weight}kg in {days} days= {total_calories}")
            
            result=f"total calorie to maintain current weight {round(calories)}"
            
            result2=f"total calorie to intake to {mode} in {days} = {round(total_calories)}"
            
            
            
        return render(request,self.template_name,{
                                                  "form":form_instance,"calorie":total_calories,
                                                  "result":result,
                                                  "result2":result2
                                                  }
                      )

class MilageView(View):
    
    template_name="milage.html"
    
    def get(self,request,*args,**kwargs):
        
        form_instance=MilageForm
        
        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        
        form_data=request.POST
        
        form_instance=MilageForm(form_data)
        
        if form_instance.is_valid():
            
            data=form_instance.cleaned_data
            
            distance_travel=data.get("distance_travel")
            
            fuel_consumed=data.get("fuel_consumed")
            
            mileage=distance_travel/fuel_consumed
            
            result=f"milage {mileage}"
            
        return render(request,self.template_name,{"form":form_instance,"result":result})
    
class PercentageView(View):
    
    template_name="calculator.html"
    
    form_class=PercentageForm
    
    def get(self,request,*args,**kwargs):
        
        form_instance=self.form_class()
        
        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        
        form_data=request.POST
        
        form_instance=PercentageForm(form_data)
        
        if form_instance.is_valid():
            
            data=form_instance.cleaned_data
            
            amount=data.get("amount")
            
            percentage=data.get("percentage")
            
            calc=percentage/100*amount
            
            result=f"percentage of the amount = {calc}"
            
        return render(request,self.template_name,{"form":form_instance,"result":result})
    
class ConversionView(View):
    
    template_name="temp.html"
    
    form_class=ConversionForm
    
    def get(self,request,*args,**kwargs):
        
        form_instance=self.form_class()
        
        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        
        form_data=request.POST
        
        form_instance=ConversionForm(form_data)
        
        if form_instance.is_valid():
            
            data=form_instance.cleaned_data
            
            degree_celcius=data.get("degree_celcius")
            
            farehnheit=data.get("farehnheit")
            
            # F = (°C x 9/5) + 32
            
            # farehnheit=(degree_celcius*9/5)+32
            
            temp_degree=degree_celcius*(9/5)+32
            
            temp_farehnheit=(farehnheit-32)*5/9
            
            result=0
            
            result2=0
            
            result=f"degree celsius to fh ={temp_degree}"
            
            result2=f"fahrenheit to degree celsius = {temp_farehnheit}"
            
        return render(request,self.template_name,{
                                                  "form":form_instance,
                                                  "result":result,
                                                  "result2":result2
                                                  }
                      )
            
        # (f-32)*5/9
        
class LeapyearView(View):
    
    template_name="year.html"
    
    form_class=LeapyearForm
    
    def get(self,request,*args,**kwargs):
        
        form_instance=self.form_class()
        
        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        
        form_data=request.POST
        
        form_instance=LeapyearForm(form_data)
        
        if form_instance.is_valid():
            
            data=form_instance.cleaned_data
            
            year=data.get("year")
            
            result=0
            
            result2=0
            
            if year%4==0 and year%100!=0:
                
                result=f"leap year{year}"
                
            else:
                
                result2=f"not leap year {year}"
                
        return render(request,self.template_name,{"form":form_instance,"result":result,"result2":result2})
    
class SignupView(View):
    
    template_name="sign.html"
    
    form_class=SignupForm
    
    def get(self,request,*args,**kwargs):
        
        form_instance=self.form_class()
        
        return render(request,self.template_name,{"form":form_instance})
    
class CustomerView(View):
    
    template_name="customer.html"
    
    form_class=CustomerForm
    
    def get(self,request,*args,**kwargs):
        
           form_instance=self.form_class()
           
           return render(request,self.template_name,{"form":form_instance})
       
class IndexView(TemplateView):
    
    template_name="index.html"