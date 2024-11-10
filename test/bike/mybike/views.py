from django.shortcuts import render,redirect,get_object_or_404

from django.views.generic import View

from mybike.forms import BikeForm

from mybike.models import BikeModel

# Create your views here.


class BikeCreateView(View):
    
    template_name="bike_add.html"
    
    form_class=BikeForm
    
    def get(self,request,*args,**kwargs):
        
        form_instance=self.form_class()
        
        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        
        form_data=request.POST
        
        form_instance=self.form_class(form_data,files=request.FILES)
        
        if form_instance.is_valid():
            
            form_instance.save()
            
            return redirect("bike-list")
        
        return render(request,self.template_name,{"form":form_instance})
    
class BikeListView(View):
    
    template_name="bike_list.html"
    
    def get(self,request,*args,**kwargs):
        
        qs=BikeModel.objects.all()
        
        return render(request,self.template_name,{"data":qs})
    
class BikeDeleteView(View):
    
    def get(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        get_object_or_404(BikeModel,id=id).delete()
        
        return redirect("bike-list")
    
class BikeDetailView(View):
    
    template_name="bike_detail.html"
    
    def get(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        qs=get_object_or_404(BikeModel,id=id)
        
        return render(request,self.template_name,{"data":qs})
    
class BikeUpdateView(View):
    
    template_name="bike_update.html"
    
    form_class=BikeForm
    
    def get(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        bike_object=get_object_or_404(BikeModel,id=id)
        
        form_instance=self.form_class(instance=bike_object)
        
        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        bike_object=get_object_or_404(BikeModel,id=id)
        
        form_data=request.POST
        
        form_instance=self.form_class(form_data,files=request.FILES,instance=bike_object)
        
        if form_instance.is_valid():
            
            form_instance.save()
            
            return redirect("bike-list")
        
        return render(request,self.template_name,{"form":form_instance})
    

        
        
    
    