text="mdhekwfkfkjhfkfkjrfbaeiou"

vowels="aeiou"

v_count=0

text=text.casefold()


for ch in text:
    
    if vowels.count(ch)!=0:
        
        v_count+=1   
        
print(v_count)
        
   