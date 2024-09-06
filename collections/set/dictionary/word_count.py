
# word=["hello","hello","hi","hai","hai"]

# word_count=len(word)

# for i in word:
    
#     word_count=i.


word=["hello","hi","hello","hai","hai"] 

word_count={}

for w in word:
    
    if w in word_count:
    
       word_count[w]+=1
       
    else:
    
     word_count[w]=1
    
print(word_count)  

