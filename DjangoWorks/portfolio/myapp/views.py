from django.views.generic import View

from django.shortcuts import render


class IndexView(View):
    
    def get(self,request,*args,**kwargs):
        
        
        person_data={
            
            "id":1,
            "age":20,
            "name":"nzm",
            "location":"pkd",
            "address":"street37"
        }
        
        return render(request,'index.html',{"person":person_data})
    

class ProjectView(View):
    
    def get(self,request,*args,**kwargs):
        
        
        projects=[
            {"id":1,"title":"codehub",
             "description":"project decsription",
             "front_end":"react","back_end":"django"
             },
              {"id":2,"title":"ServiceHub",
             "description":"project decsription",
             "front_end":"Angular","back_end":"django"
             },
              {"id":3,"title":"linksphere",
             "description":"project decsription",
             "front_end":"react","back_end":"django"
             }
        ]
        
        return render(request,'project.html',{"project":projects})
    
class ContactView(View):
    
    def get(self,request,*args,**kwargs):
        
        person_mail="nazeempm7@gmail.com"
        
        person_num=5377333
        
        person_address="steet35"
        
        person_place='newjersy'
        
        return render(request,'contact.html',{"email":person_mail,"num":person_num,"address":person_address,"place":person_place})
    

class SkillsView(View):
    
    def get(self,request,*args,**kwargs):
        
        project_backend="python django"
        
        project_framework="react"
        
        project_database="Mysql"
        
        return render(request,'skill.html',{'backend':project_backend,"framework":project_framework,"database":project_database})
    

class ServiceView(View):
    
    def get(self,request,*args,**kwargs):
        
        services=["webapplication development","Api development","ui","ux"]
        
        return render(request,"service.html",{"services":services})
    
    
    

