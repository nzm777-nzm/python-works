num=int(input("enter a number"))

result=0

palindrome=num

while(num!=0):
    
    digit=num%10
    
    result=result*10+digit
    
    num=num//10
    
print(result)

print("num is palindrom" if palindrome==result  else "not palindrome" )