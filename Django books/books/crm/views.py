from django.shortcuts import render,redirect,get_object_or_404

from django.views.generic import View

from crm.forms import BookForm,BookUpdateForm,SignInForm,SignupForm

from crm.models import Books

from django.db.models import Q

from django.contrib.auth.models import User

from django.contrib.auth import login,logout,authenticate

from django.views.decorators.cache import never_cache

from crm.decorators import signin_required

from django.utils.decorators import method_decorator

from django.contrib import messages

# Create your views here.

decs=[never_cache,signin_required]

@method_decorator(decs,name="dispatch")
class BookView(View):
    
    template_name="books.html"
    
    form_class=BookForm
    
    def get(self,request,*args,**kwargs):
        
        form_instance=self.form_class()
        
        return render(request,self.template_name,{"form":form_instance})
    
    
    def post(self,request,*args,**kwargs):
        
        form_data=request.POST
        
        form_instance=self.form_class(form_data,files=request.FILES)
        
        if form_instance .is_valid():
            
            data=form_instance.cleaned_data
            
            print(data)
            
            Books.objects.create(**data)
            
            messages.success(request,"book added successfully")
            
            return redirect("book-list")
        
        messages.error(request,"sorry added failed")
            
        return render(request,self.template_name,{"form":form_instance})
 
@method_decorator(decs,name="dispatch")   
class BooksListView(View):
    
    template_name="book_list.html"
    
    def get(self,request,*args,**kwargs):
        
        search_text=request.GET.get("filter")
        
        qs=Books.objects.all()
        
        if search_text:
            
            qs=qs.filter(
                
                Q(name__contains=search_text)|Q(author__contains=search_text)|Q(category__contains=search_text)
            )
            
        
        return render(request,self.template_name,{"data":qs})
    
@method_decorator(decs,name="dispatch")
class BookDetailView(View):
    
    template_name="book_detail.html"
    
    def get(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        qs=Books.objects.get(id=id)
        
        return render(request,self.template_name,{"data":qs})

@method_decorator(decs,name="dispatch")
class BookDeleteView(View):
    
    def get(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        qs=Books.objects.get(id=id).delete()
        
        messages.success(request,"deleted succesfully")
        
        return redirect("book-list")
    
# class BookUpdateView(View):
    
    template_name="book_update.html"
    
    form_class=BookForm
    
    def get(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        Books_object=Books.objects.get(id=id)
        
        data={
            
            "name":Books_object.name,
            
            "price":Books_object.price,
            
            "author":Books_object.author,
            
            "category":Books_object.category
        }
        
        form_instance=self.form_class(initial=data)
        
        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        form_data=request.POST
        
        form_instance=self.form_class(form_data)
        
        if form_instance.is_valid():
            
            data=form_instance.cleaned_data
            
            Books.objects.filter(id=id).update(**data)
            
            return redirect("book-list")
        
        return render(request,self.template_name,{"form":form_instance})
    
@method_decorator(decs,name="dispatch")
class BookUpdateView(View):
    
    template_name="book_update.html"
    
    form_class=BookUpdateForm
    
    def get(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        book_object=get_object_or_404(Books,id=id)
        
        form_instance=self.form_class(instance=book_object)
        
        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        book_object=get_object_or_404(Books,id=id)
        
        form_data=request.POST
        
        form_instance=self.form_class(form_data,request.FILES,instance=book_object)
        
        if form_instance.is_valid():
            
            form_instance.save()
            
            messages.success(request,"book updated successfully")
            
            return redirect(request,"book-list")
        
        messages.error(request,"sorry failed")
        
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
            
            messages.success(request,"registered successfully")
            
            return redirect("register")
        
        messages.error(request,"failed!!")
        
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
            
            #check credentials valid or not
            
            user_object=authenticate(request,username=uname,password=pwd)
            
            if user_object:
                
                login(request,user_object)
                
                messages.success(request,"logged succesfully")
                
                return redirect("book-list")
            
            messages.error(request,"login failed")
            
        return render(request,self.template_name,{"form":form_instance})

@method_decorator(decs,name="dispatch")
class SignOutView(View):
    
    def get(self,request,*args,**kwargs):
        
        logout(request)
        
        
        return redirect("signin")
            
                  
            
            
           
        
        
        
    