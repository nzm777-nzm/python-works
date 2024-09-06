
from re import finditer

text="abc 7klefg@#"

# pattern="\\d"  #only digits

# pattern=r"\D"  #remove digits and show aplaha and special char

# pattern=r"\w" # remove spechial char

# pattern=r"\W"  #remove aplha numeric show special char

pattern=r"\s"

matcher=finditer(pattern,text)

for m in matcher:
    
    print(m.start(),"===",m.group())