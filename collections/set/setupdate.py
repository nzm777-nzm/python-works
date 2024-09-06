
names={"hello","hi","suiii"}

new_name={"hello","tt","aa"}

names.update(new_name) #add elements from any collection to the set

print(names)

new_set=names.union(new_name) #return the element from the two sets and return as new one

print(new_set)

new_set=names.intersection(new_name) #return common elements from 2 set objects as a new set

print(new_set)

new_set=names.difference(new_name) #return elements from set names which is not in the set as new set

print(new_set)

new_set=names.symmetric_difference(new_name)

print(new_set)
