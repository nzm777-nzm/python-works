
from re import finditer

text="abd123 @k#7LMdef"

#pattern="[abf]" #chck for ab or ie f

# pattern="[@123]"

# pattern="[a-k]" chck for all lower case aplphabets

# pattern="[a-zA-Z]"  chck for all upper case aplphabets

# pattern="[a-zA-Z0-9]" #chck for all alphanumeric char

# pattern="[^0-9]"

# pattern="[^a-zA-z0-9]"

# pattern="[\s]"

pattern="[^a-zA-Z0-9\s]"

matcher=finditer(pattern,text)

for m in matcher:
    
    print(m.start(),"===",m.group())
    
    