
def armstrong(num):
    
    total=0
    
    original=num
    
    digit_count=len(str(num))
    
    while(num!=0):
    
        digit=num%10
        
        exponent=digit ** digit_count
        
        total=total+exponent
        
        num=num//10
        
        result=original
    
    return result  if result==total  else "no armstrong "

print(armstrong(num=153))