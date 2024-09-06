
# arr=[10,11,12,13,14,15,16,17]

# new=[]

# odd_pos_num=[ for n in arr if n]

# odd_num.reverse()



arr=[10,11,12,13,14,15,16,17,18]

left=1

length=len(arr)-1

if length%2!=0:
    
    right=length
    
else:
    
    right=length-1
    
    
while(left<right):
    
    (arr[left],arr[right])=(arr[right],arr[left])
    
    left=left+2
    
    right=right-2

print(arr)

