

# 1st character upper case aplhabet

# next character digit from 1-9

#next digit  0- 9

# 4th place 0 or 1 space

# next 4 characters any number from 0 to 9

# last character 1-9

# S71 19937

from re import fullmatch

passport_id=input("enter passport id :")

pattern=r"[A-Z][1-9]\d[0\s]\d{4}[1-9]{1}"

matcher=fullmatch(pattern,passport_id)

print("invalid" if matcher==None else "valid")


