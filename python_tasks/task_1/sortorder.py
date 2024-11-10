num1=int(input("enter a number"))

num2=int(input("enter a number "))

num3=int(input("enter a number"))

if num1>num2:
    
    num1,num2=num2,num1
    
if num1>num3:
    
    num1,num3=num3,num1
    
if num2>num3:
    
    num2,num3=num3,num2
    
print(num1 , "<", num2, "<",num3 ) 
        
 
    

