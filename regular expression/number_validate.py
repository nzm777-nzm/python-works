
# country code

# number start with 678

from re import fullmatch

ph_num=input("enter ph num :")

pattern=r"(91)(-)?[6-9]\d{9}"

matcher=fullmatch(pattern,ph_num)

print("invalid" if matcher==None else "valid")
