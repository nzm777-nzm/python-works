
from django.views.generic import View

from django.http import HttpResponse

from django.shortcuts import render

class HelloWorldView(View):
    
    def get(self,request,*args,**kwargs):
        
        return HttpResponse("hello world")
    
class GoodMorning(View):
    
    def get(self,request,*args,**kwargs):
        
        return HttpResponse("have a nice day !!")

class GoodAfterNoon(View):
    
    def get(self,request,*args,**kwargs):
        
        return HttpResponse("good afternoon")
    
class GoodEvening(View):
    
    def get(self,request,*args,**kwargs):
        
        return HttpResponse("good evening")
    
class GoodNight(View):
    
    def get(self,request,*args,**kwargs):
        
        return HttpResponse("goodnight")
    
class SelfIntroView(View):
    
    def get(self,request,*args,**kwargs):
        
        return render(request,"selfintro.html")
    
class FrameWorkView(View):
    
    def get(self,request,*args,**kwargs):
        
        return render(request,"framework.html")
    
    

#mobiles

#car

class Car(View):
    
    def get(self,request,*args,**kwargs):
        
        return render(request,"vehicle.html")
    
class MobilesView(View):
    
    def get(self,request,*args,**kwargs):
        
        return render(request,"mobiles.html")