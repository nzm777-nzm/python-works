
from json import load

f=open("C:\\Users\\HP\\Desktop\\python_june_works\\jsonworks\\country.json",encoding="UTF-8")

data=load(f)

def fetch_country_details(name):
    
    return [c for c in data if c.get("name")==name]

country_data=fetch_country_details("Afghanistan")

