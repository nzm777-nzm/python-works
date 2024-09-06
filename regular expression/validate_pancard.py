
# validate pan card

# first 3 letter are alphabets

# 4th place PCAFHT

# 5th place alphabet

# 4 digit

# 1 alphabet

from re import fullmatch

pancard=input("enter your pan number")

pattern=r"[A-Z]{3}[PCAFHT][A-Z]\d{4}[A-Z]{1}"

matcher=fullmatch(pattern,pancard)

print("invalid" if matcher==None else "valid")

