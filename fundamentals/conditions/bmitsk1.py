weight_in_kg=int(input("enter weightkg: "))

height_in_cm=int(input("enter your height: "))

height_in_meter=height_in_cm/100

bmi=(weight_in_kg)/(height_in_meter**2)

print(f"bmi of a person bmi: {bmi}")


