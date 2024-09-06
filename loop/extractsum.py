num=int(input("enter a number"))

sum=0

while(num%10!=0):
    digit=num%10
    sum=sum+digit
    print(digit)
    num=num//10
print(sum)