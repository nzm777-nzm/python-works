num=int(input("enter a number"))

previous=0

current=1

is_fibo=False

if num in (0,1):
    
    is_fibo=True
    
else:
       
    next=previous+current

    while(next<=num):
        
        next=previous+current
        
        previous=current
        
        current=next
        
        if next==num:
            
            is_fibo=True
            
            break
        
print(is_fibo)



        
