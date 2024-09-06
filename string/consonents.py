text="ahelliou"

vowels="aeiou"

v_count=0

c_count=0

text=text.casefold()



for ch in text:
    
    if vowels.count(ch)!=0:
        
        v_count+=1  
        
    else:
        c_count+=1
        
print(v_count)
print(c_count)
        
   