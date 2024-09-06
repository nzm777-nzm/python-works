
from re import fullmatch

variable_name=input("enter variable name :")

pattern=r"[k-mK-M][369][a-zA-Z0-9@]*"

matcher=fullmatch(pattern,variable_name)

print("invalid" if matcher==None else "valid")