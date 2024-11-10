from django.contrib import messages

from django.shortcuts import redirect


def signin_required(fn):
    
    #inner function
    
    def wrapper(request,*args,**kwargs): #parameter enter
        
        
        #logic apply
        
        if not request.user.is_authenticated:         
            
            messages.error(request,"failed try again")
            
            return redirect("signin")
        else:
            
            return fn(request,*args,**kwargs)
        
    return wrapper

            