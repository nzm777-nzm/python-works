from django.shortcuts import render,redirect,get_object_or_404

from django.views.generic import View

from store.forms import VehicleForm,VehicleUpdateForm,SignupForm,SignInForm

from store.models import Vehicle

from django.db.models import Q

from django.contrib.auth.models import User



# Create your views here.

class VehicleCreateView(View):
    
    template_name="vehicle_add.html"
    
    form_class=VehicleForm
    
    def get(self,request,*args,**kwargs):
        
        form_instance=self.form_class()
        
        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        
        form_data=request.POST
        
        form_instance=self.form_class(form_data,files=request.FILES)
        
        if form_instance .is_valid():
            
            data=form_instance.cleaned_data
            
            print(data)
            
            Vehicle.objects.create(**data)
            
            return redirect("vehicle-list")
        
        return render(request,self.template_name,{"form":form_instance})

class VehicleListView(View):
    
    template_name="vehicle_list.html"
    
    def get(self,request,*args,**kwargs):
        
        search_text=request.GET.get("filter")
          
        qs=Vehicle.objects.all()
        
        all_names=Vehicle.objects.values_list("name",flat=True).distinct()
        
        
        all_brands=Vehicle.objects.values_list("brand",flat=True).distinct()
        
        
        all_fuel_type=Vehicle.objects.values_list("fuel_type",flat=True).distinct()
        
        
        all_owner_type=Vehicle.objects.values_list("owner_type",flat=True).distinct()
        
        
        all_records=[]
        
        
        all_records.extend(all_names)
        
        
        all_records.extend(all_brands)
        
        
        all_records.extend(all_owner_type)
        
        
        all_records.extend(all_fuel_type)
        
        
        if search_text:
            
            qs=qs.filter(
                
                Q(name__contains=search_text)|Q(fuel_type__contains=search_text)|
                
                Q(owner_type__contains=search_text)
            )
        
        return render(request,self.template_name,{"data":qs,"records":all_records})
    

class VehicleDetailView(View):
    
    template_name="vehicle_detail.html"
    
    def get(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        qs=Vehicle.objects.get(id=id)
        
        return render(request,self.template_name,{"data":qs})
    
class VehicleDeleteView(View):
    
    def get(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        Vehicle.objects.get(id=id).delete()
        
        return redirect("vehicle-list")
    
# class VehicleUpdateView(View):
    
#     template_name="vehicle_update.html"
    
#     form_class=VehicleForm
    
#     def get(self,request,*args,**kwargs):
        
#         id=kwargs.get("pk")
        
#         vehicle_object=Vehicle.objects.get(id=id)
        
#         data={
            
#             "name":vehicle_object.name,
            
#             "varient":vehicle_object.varient,
            
#             "description":vehicle_object.description,
            
#             "fuel_type":vehicle_object.fuel_type,
            
#             "running_km":vehicle_object.running_km,
            
#             "color":vehicle_object.color,
            
#             "price":vehicle_object.price,
            
#             "brand":vehicle_object.brand,
            
#             "owner_type":vehicle_object.owner_type
#         }
        
        
#         form_instance=self.form_class(initial=data)
        
#         return render(request,self.template_name,{"form":form_instance})
    
#     def post(self,request,*args,**kwargs):
        
#         id=kwargs.get("pk")
        
#         form_data=request.POST
        
#         form_instance=self.form_class(form_data,files=request.FILES)
        
#         if form_instance.is_valid():
            
#             data=form_instance.cleaned_data
            
#             Vehicle.objects.filter(id=id).update(**data)
            
#             return redirect("vehicle-list")
        
#         return render(request,self.template_name,{"form":form_instance})
            
            
class  VehicleUpdateView(View):
    
    template_name="vehicle_update.html"
    
    form_class=VehicleUpdateForm
    
    def get(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        vehicle_object=get_object_or_404(Vehicle,id=id)
        
        form_instance=self.form_class(instance=vehicle_object)
        
        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        vehicle_object=get_object_or_404(Vehicle,id=id)
        
        form_data=request.POST
        
        form_instance=self.form_class(form_data,files=request.FILES,instance=vehicle_object)
        
        if form_instance.is_valid():
                        
            form_instance.save()
            
            return redirect("vehicle-list")
        
        return render(request,self.template_name,{"form":form_instance})
            

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
            
        
    