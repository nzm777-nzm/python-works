
numbers=[10,10,20,30,4,5]

word_count={}

for c in numbers:
    
    if c in word_count:
        
        word_count[c]+=1
        
    else:
        
        word_count[c]=1

for k,v in word_count.items():
    
    if v==1:
        
        print(k)