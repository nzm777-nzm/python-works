
from re import finditer

text="aBcDeFgHiJKlMnOpQrStUvWxYz"

pattern="[a-zA-z]"

matcher=finditer(pattern,text)

for m in matcher:
    
    print(m.start(),"===",m.group())
    