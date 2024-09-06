
from re import finditer

text="haihellohaihellohaihello"

matcher=finditer("hai",text)

count=0

for m in matcher:
    
    print(m.start(),"===",m.group())#(0,hai)
    
    count+=1

print(f"total count={count}")


