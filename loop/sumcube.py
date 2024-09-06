num=int(input("enter a number"))

sum=0

while(num%10!=0):
    
    digit=num%10
    
    cube=digit ** 3
    
    sum=sum+cube
    
    print(digit)
    
    num=num//10
    
print(sum)    
    