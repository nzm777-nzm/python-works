
# 4)Write  a program for grade classification based on percentage 
# conditions 
#   percentage = 90
#   grade A
#  percentage in between 80-90 
# grade B
# percentage in between 70-80 
# grade C 
# percentage less than 70 
# # fail 

percentage=int(input("enter your percentage"))

if percentage==90:
    
    print(percentage,"grade A")

elif percentage in range(80,91):
    
    print(percentage,"grade B")
    
elif percentage in range(70,81):
    
    print(percentage,"grade C")
    
elif percentage < 70:
    
    print(percentage,"fail")