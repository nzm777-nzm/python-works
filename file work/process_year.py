
f_read=open("C:\\Users\\HP\\Desktop\\python_june_works\\file work\\years.txt","r")

f_centuary=open("C:\\Users\\HP\\Desktop\\python_june_works\\file work\\centuary.txt","w")

f_non_centuary=open("C:\\Users\\HP\\Desktop\\python_june_works\\file work\\non_centuary.txt","w")

for year in f_read:
    
    y=int(year.rstrip("\n"))
    
    if y%100==0:
        
        f_centuary.write(str(y)+"\n")
        
    else:
        
        f_non_centuary.write(str(y)+"\n")