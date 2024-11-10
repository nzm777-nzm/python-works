


num1=int(input("enter a number1"))

num2=int(input("enter a number2"))

try:
    
    result=num1/num2
    
    print(result)
    
except Exception as e:
    
    num2=int(input("enter number 2"))
    
    result=num1/num2
    
    print(result)

finally:
    
    print("file trasfer")
    
    print("db commit")
