
text="ABACDDBB"

word_count={}

for c in text:
    
    if c in word_count:
        
        print(c ,"first recursive ")
        
        break
    
    else:
        
        word_count[c]=1
        
        
        