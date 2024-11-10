
from json import load

f=open("C:\\Users\\HP\\Desktop\\python_june_works\\jsonworks\\filims.json")

movies=load(f)

for m in movies:
    
    titles=(m.get("title"))
    
    years=(m.get("rating"))
    
    print(titles,years)

