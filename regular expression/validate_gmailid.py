

# gmail id pattern

from re import fullmatch

gmail_id=input("enter your gmail id :")

# pattern=r"\w+(@gmail.com)"

pattern=r"\w[\w\._]*@gmail.com"

matcher=fullmatch(pattern,gmail_id)

print("invalid" if matcher==None else "valid")

# + match one or more

# ? optional

# * zero or more

