
from re import finditer

text="ab12xyz678#$pqr123cdef"

# pattern="[a-z]{3}"

# pattern="[0-9]{3}"

# pattern="[^a-z0-9]"

# pattern="([c-h]|[t-z])"

pattern="([a-z]{3}|[0-9]{3})"

matcher=finditer(pattern,text)

for m in matcher:
    
    print(m.start(),"===",m.group())
