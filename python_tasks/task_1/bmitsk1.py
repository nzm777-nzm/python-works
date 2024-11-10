weight_in_kg=int(input("enter weightkg: "))

height_in_cm=int(input("enter your height: "))

height_in_meter=height_in_cm/100

bmi=(weight_in_kg)/(height_in_meter**2)

print(f"bmi of a person : {bmi}")

if bmi<=19:
    
    print("under weight")
    
elif bmi <=25:
    
    print("normal weight") 
    
if bmi <=30: 
    
    print("over weight")
   
else:         
     print("obesity")      
    
    
       
    



