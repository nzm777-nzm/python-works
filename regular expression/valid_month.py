
from re import fullmatch

months=input("enter a month :")

pattern=r"(0?[0-9]|[1][0-2])"

matcher=fullmatch(pattern,months)

print("invalid" if matcher==None else "valid")