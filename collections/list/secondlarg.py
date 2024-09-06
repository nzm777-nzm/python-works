
num=[1,2,3,4,5,6,7,8,11,10]

largest_num=0

second_larg=0

for i in num:
    
    if i > largest_num and i > second_larg: 
        
        second_larg = largest_num
        
        largest_num = i

    elif i > second_larg and i < largest_num:
        
      second_larg=i
      
      print(second_larg)


# wap  to find the sum of odd numbers

# wap to find the count of even and odd numbers in the list
