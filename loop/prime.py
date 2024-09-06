num=int(input("enter a number"))

isprime=True

for i in range(2,num):
    
   if num%i==0:
       
       isprime=False
       
       break
       
print(f"{num} is prime" if isprime==True else f"{num} not prime")
       
       
        