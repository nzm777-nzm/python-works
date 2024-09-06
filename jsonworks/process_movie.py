from json import load

f=open("C:\\Users\\HP\\Desktop\\python_june_works\\jsonworks\\filims.json")

movies=load(f)

for m in movies:
    
    print(m.get("title"))

