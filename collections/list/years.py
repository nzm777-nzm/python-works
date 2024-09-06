
years=[1000,1001,2000,2004,2001,2008,2016,2028,1800]

for i in range(0,len(years)):
    
    if years[i]%100==0 and years[i]%400==0 and years[i]%100!=0 and years[i]%4==0:
        
        print(years[i])
        
            
    
        
    