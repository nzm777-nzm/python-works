
from re import fullmatch

vehicle_num=input("enter a ehicle num: ")

# pattern=r"(KL)\d{2}[A-Z]{1,2}\d{4}"

pattern=r"(KL)(-)?[0-9]{2}(-)?[A-Z](-)?{1,2}(-)?[0-9]{4}"

matcher=fullmatch(pattern,vehicle_num)

print("invalid" if matcher==None else "valid")

# vehicle_number=input("enter vehicle num :")

# pattern=r"[A-Z]{1,2}\d{2}[A-Z]{1,2}\d{4}"

# matcher=fullmatch(pattern,vehicle_number)

# print("invalid" if matcher==None else "valid")



