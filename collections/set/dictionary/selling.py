
mobiles={"name":"i phone14","brand":"apple","price":20000,"is_avilable":True,"offer":1000}

if "offer" in mobiles:
    
    selling_price=mobiles.get("price")-mobiles.get("offer")
    
    print(selling_price)
    
else:
    
    selling_price=mobiles.get("price")
    
    print(selling_price)