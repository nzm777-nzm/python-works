
 
# # text1=list=["{", "}", "[", "]", "(", ")"]

# # text2=list=["}", "(", "]","{", "[", ")"]

# text1=list=["[ { ( ) } ]"]

# text2=list=["{ ) [ ( ] }"]

# valid=[" [ { ( ) } ] "]

# unvalid=[" ( } [ { ) ] "]


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# common perfix

# words=["fly","float","flower","flat"]

# smallest_word=words[0]

# for w in words:
    
#     if w in smallest_word:
        
#         prefix=smallest_word[:-1]
        
# print(prefix)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# kangaroooooooooooooooooooooooooooo

# source_word="chicken"

# target_word="hen"

# word_count={}

# for w in source_word:
    
#     if w in target_word:
        
#         word_count[w]=+1
        
#     else:
        
#         word_count[w]=1
        
# is_kangaroo=True

# for w in target_word:
    
#     if w in word_count and word_count.get(w)>0:
        
#         word_count[w]=-1
        
#     else:
        
#         is_kangaroo=False
        
# print(is_kangaroo)

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                      
                        #    RECURSIVE


#    q  # {'hello': 3, 'hai': 2}

# text="hello hai hello hai hello"

# count={}

# splited=text.split(" ")


# for w in splited:
    
#     if w in count:
        
#         count[w]+=1
        
#     else:
        
#         count[w]=1
        
# print(count)
        
        
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 
                        # FIRST RECURSIVE
                        #    expected_output=A first recursive 


# text="ABACDDBB"

# recursive={}

# for w in text:
    
#     if w in recursive:
        
#         print(w,"recursive")
        
#         break
#     else:
        
#         recursive[w]=1
        

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
       
                                # NON_RECURSIVE
                                
                                #   expected_output=aabbcde = cde
                                
# text="ABBABCDE"

# count={}

# for w in text:
    
#     if w in count:
        
#         count[w]+=1
        
#     else:
        
#         count[w]=1
        
# for k,v in count.items():
    
#     if v==1:
        
#         print(k)



        
        
        
      
        
        
        
   
        
        
        
        
        
    
        
   

        
        
        




        
        
        
      
      

            
            
        
        