
f=open("C:\\Users\\HP\\Desktop\\python_june_works\\file work\\news.txt","r")

word_lisst=[w for line in f for w in line.rstrip("\n").split(" ") if w!=""]

wc={w:word_lisst.count(w) for w in word_lisst}

# print(wc)

def get_value(key):
    
    return wc.get(key)

srt=sorted(wc,key=get_value,reverse=True)

print(srt)


# print(word_lisst)

# word_lst=[]

# for line in f:
    
#     words=line.strip("\n").split(" ")
    
#     for w in words:
        
#         word_lst.append(w)
        
# print(word_lst)