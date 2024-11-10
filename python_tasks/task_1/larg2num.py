num1=int(input("enter a number"))

num2=int(input("enter a number"))

num3=int(input("enter a number"))

if num2>num1>num3 or num3>num1>num2:
    
    print(f"second largest is: {num1} ") 
    
elif num1>num2>num3 or num3>num2>num1:
    
    print(f"second larset number:{num2}")   

elif num1>num3>num2 or num2>num3>num1:
    
    print(f"second largest number:{num2}")       
    