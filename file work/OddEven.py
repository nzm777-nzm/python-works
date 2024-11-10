

f=open("C:\\Users\\HP\\Desktop\\python_june_works\\file work\\OddEven.txt","w")

for num in range(0,101):
    
    if num%2==0:
        
        f.write(str(num)+"\n")
    
    