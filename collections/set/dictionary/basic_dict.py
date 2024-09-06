# dict={"key":"value"} #key should be unique

student={"name":"suii","course":"fullstack","course":"django"} #overwrites 

# <class dict> : collection of elements as a key:value pair

# print(student["name"])

# print(student.keys())

student["name"]="trever" # update the value

student["place"]="china"  #overwrites the value if the key is present else add as a new pair        

print(student)

new=student.items()

print(new)

