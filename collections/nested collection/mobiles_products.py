
mobiles=[

    {"id":100,"title":"s23 ultra","brand":"samsung","price":125000,"network":"5g"},
    
    {"id":101,"title":"s23","brand":"samsung","price":54000,"network":"4g"},
    
    {"id":102,"title":"edge14pro","brand":"moto","price":25000,"network":"5g"},
    
    {"id":103,"title":"edgeneo","brand":"moto","price":22000,"network":"4g"},
    
    {"id":104,"title":"redminote13pro","brand":"mi","price":25000,"network":"5g"},
    
    {"id":105,"title":"redmi13","brand":"mi","price":12000,"network":"4g"},
]

# all_mobile_names=[mob.get("title") for mob in mobiles]

# # print(all_mobile_names)

# all_brands=[mob.get("brand") for mob in mobiles]

# # print(all_brands)

# samsung_mob=[mob.get("title") for mob in mobiles if mob.get("brand")=="samsung"]

# # print(samsung_mob)

# price=[mob.get("title") for mob in mobiles if mob.get("price") in range(23000,40001)]

# # print(price)

max_price=0

for mob in mobiles:
    
    if mob.get("price") > max_price:
        
        max_price=mob.get("price")

high_price=[mob for mob in mobiles if ]



