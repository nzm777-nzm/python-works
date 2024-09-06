
from re import fullmatch

f=open("C:\\Users\\HP\\Desktop\\python_june_works\\regular expression\\domain.txt")

# pattern=".*.com"

pattern="[\w\W]+\\.com"

for line in f:
    
    domain=line.rstrip("\n")
    
    matcher=fullmatch(pattern,domain)
    
    if matcher !=None:
    
     print(domain)
