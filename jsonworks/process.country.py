
from json import load

f=open("C:\\Users\\HP\\Desktop\\python_june_works\\jsonworks\\country.json",encoding="UTF-8")

#total country names ..
#most highest population country ..
#country region and name x
#country native name
#independent country ..
#currency codes,symbol,
#country capital
#sub regions
#country borders
#country flags
#country language == english
#most highest area name 
#asia region ..
#asia population 
#all country timezone ..

total_country=load(f)

all_country=[c.get("name") for c in total_country]

print(all_country)
    
def most_population(dic):
    
    return dic.get("population")

highest_population=max(total_country,key=most_population)

print(highest_population.get("name"))

indipendent_country=[c.get("name") for c in total_country if c.get("independent")==True]

print(indipendent_country)

asian_region=[c.get("name") for c in total_country if c.get("region")=="Asia"]

print(asian_region)

afgan_native=[c.get("nativeName") for c in total_country if c.get("numericCode")=="004"]

print(afgan_native)

eng_language=[c.get("name") for c in total_country if c.get("languages")=="English"]

print(eng_language)

def high_area(dic):
    
    if "area" in dic:
        
        return dic.get("area")
    
    else:
        
        return 0
    
highest_areas=max(total_country,key=high_area)

print(highest_areas.get("name"))

all_regions={c.get("region") for c in total_country}

print(all_regions)

region_summary={}

for c in total_country:
    
    region_name=c.get("region")
    
    if region_name in region_summary:
        
        region_summary[region_name]+=c.get("area",0)
        
    else:
        
        region_summary[region_name]=c.get("area",0)
    
value_key=[(v,k) for k,v in region_summary.items()]

print(max(value_key))
    
    






        
        























