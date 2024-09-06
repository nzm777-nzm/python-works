
numbers=[1,2,[3,(100,200,300),4],5,6]

num=numbers[2]

ele_four=num.pop()

num.insert(1,ele_four)

new=numbers[2][2]

l1=list(new)

l1.insert(1,150)

l2=tuple(l1)

numbers[2][2]=l2

print(numbers)






