
from re import fullmatch

f=open("C:\\Users\\HP\\Desktop\\python_june_works\\regular expression\\vehicle.txt")

pattern=r"(KL)( )[\d]{2}( )[\w]{1,2}( )[\d]{4}"            

for line in f:
    
    vehicle=line.rstrip("\n")
    
    matcher=fullmatch(pattern,vehicle)
    
    if matcher !=None:
        
        print(vehicle)
        
    