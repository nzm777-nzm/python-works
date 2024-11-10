from django.shortcuts import render,redirect,get_object_or_404

from django.views.generic import View

from crm.forms import EmployeeForm,SignInForm,SignupForm

from crm.models import Employee

from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout

from django.contrib import messages

from crm.decorators import signin_required

from django.utils.decorators import method_decorator

from django.views.decorators.cache import never_cache

decs=[signin_required,never_cache]

@method_decorator(decs,name="dispatch")
class EmployeeCreateView(View):
    
    template_name="emp_add.html"
    
    form_class=EmployeeForm
    
    def get(self,request,*args,**kwargs):
        
        form_instance=self.form_class()
        
        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        
        form_data=request.POST
        
        form_instance=self.form_class(form_data,files=request.FILES)
        
        if form_instance.is_valid():
            
            form_instance.save()
            
            messages.success(request,"employee added successfully")
            
            return redirect("employee-list")
        
        messages.error(request,"oops sorry !!")
        
        return render(request,self.template_name,{"form":form_instance})
 
@method_decorator(decs,name="dispatch")   
class EmployeeListView(View):
    
    template_name="emp_list.html"
    
    def get(self,request,*args,**kwargs):
        
        qs=Employee.objects.all()
        
        return render(request,self.template_name,{"data":qs})
 
@method_decorator(decs,name="dispatch")   
class EmployeeDetailView(View):
    
    template_name="emp_detail.html"
    
    def get(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        qs=get_object_or_404(Employee,id=id)
        
        return render(request,self.template_name,{"data":qs})

@method_decorator(decs,name="dispatch")
class EmployeeDeleteView(View):
    
    def get(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        get_object_or_404(Employee,id=id).delete()
        
        messages.success(request,"deleted")
        
        return redirect("employee-list")
 
@method_decorator(decs,name="dispatch")       
class EmployeeUpdateView(View):
    
    template_name="emp_update.html"
    
    form_class=EmployeeForm
    
    def get(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        employee_object=Employee.objects.get(id=id)
        
        form_instance=self.form_class(instance=employee_object)
        
        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        employee_object=Employee.objects.get(id=id)
        
        form_data=request.POST
        
        form_instance=self.form_class(form_data,files=request.FILES,instance=employee_object)
        
        if form_instance.is_valid():
            
            form_instance.save()
            
            messages.success(request,"updated successfully")
            
            return redirect("employee-list")
        
        messages.error(request,"oops failed !!!")
        
        return redirect(request,self.template_name,{"form":form_instance})
        
class SignupView(View):
    
    template_name="register.html"
    
    form_class=SignupForm
    
    def get(self,request,*args,**kwargs):
        
        form_instance=self.form_class()
        
        return render(request,self.template_name,{"form":form_instance})  
        
    
    def post(self,request,*args,**kwargs):
        
        form_data=request.POST
        
        form_instance=self.form_class(form_data)
        
        if form_instance.is_valid():
            
            data=form_instance.cleaned_data
            
            # password hash method
            
            User.objects.create_user(**data)
            
            return redirect("register")
        
        return render(request,self.template_name,{"form":form_instance})
            
class SignInView(View):
    
    template_name="signin.html"
    
    form_class=SignInForm
    
    def get(self,request,*args,**kwargs):
        
        form_instance=self.form_class()
        
        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        
        form_data=request.POST
        
        form_instance=self.form_class(form_data)
        
        if form_instance.is_valid():
            
            data=form_instance.cleaned_data
            
            uname=data.get("username")
            
            pwd=data.get("password")
            
            user_object=authenticate(request,username=uname,password=pwd)
            
            if user_object:
                
                login(request,user_object)
                
                messages.success(request,"login successfully")
                
                return redirect("employee-list")
            
            messages.error(request,"check username and")
            
        return render(request,self.template_name,{"form":form_instance})
    
@method_decorator(decs,name="dispatch")
class SignOutView(View):
        
     def get(self,request,*args,**kwargs):
            
        logout(request)
                    
        return redirect("signin")
            