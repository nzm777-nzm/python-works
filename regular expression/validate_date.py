
from re import fullmatch

date=input("enter a date :")

# pattern=r"(0)?[1-9]|[1][0-31]"

pattern=r"(0)?[1-9]|1[0-9|[2][0-9]|[3][0-1]"

matcher=fullmatch(pattern,date)

print("invalid" if date==None else "valid")

