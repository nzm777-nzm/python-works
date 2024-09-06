num=int(input("enter a number"))

sum=0

armstrong=num

digit_count=len(str(num))

while(num!=0):
    
    digit=num%10
    
    exponent=digit ** digit_count
    
    sum=sum+exponent
    
    num=num//10
    
print("armstrong number" if armstrong==sum else "not armstrong")    
    
           