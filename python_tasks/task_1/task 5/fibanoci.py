def fibo(num):

    previous=0

    current=1

    result=False

    if num in (0,1):
        
        return True
        
    else:
        
        next=previous+current

        while(next<=num):
            
            next=previous+current
            
            previous=current
            
            current=next
            
            if next==num:
                
             return True
         
        return result
    
print(fibo(20))            
                
    
            



            
