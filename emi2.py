loan_amount=int(input("enter loan amount"))

intrest=int(input("enter intrest"))

tenure=int(input("enter tenure"))

intrest=intrest/(12*100)

emi=loan_amount*intrest*((1+ intrest)**tenure) / ((1+intrest)**tenure -1)

print(f"monthly emi = {emi}")

total_intrest_payable=tenure*emi

print(f"total intrest payable = {total_intrest_payable} ")