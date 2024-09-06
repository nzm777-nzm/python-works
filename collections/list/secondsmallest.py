
numbers=[1,5,7,3,9,2,6,10,4]

smallest_num=numbers[-1]

second_small=numbers[0]

for i in numbers:
    
    if i < second_small and i < smallest_num:
        
        second_small=smallest_num
        
        smallest_num=i
    
    elif i < second_small and i > smallest_num:
        
        second_small=i
        
print(second_small)

 