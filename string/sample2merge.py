# word1="PQRS"

# word2="ABCDEFG"

word1="PQRS"

word2="ABCDEFG"

smallest_str=word1 if len(word1) < len(word2) else word2

merge_str=""

for i in range(0,len(smallest_str)):
    
    merge_str=merge_str+word1[i]+word2[i]
    
    if len(word1) < len(word2):
        
        balance=word1[len(smallest_str):]
        
    else:
        
        balance=word2[len(smallest_str):]
        
    merge_str=merge_str+balance

print(merge_str)    
        
        
    
    
    