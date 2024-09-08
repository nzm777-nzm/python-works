
class bike:
    
    name:str
    
    price:int
    
    brand:str
    
    
    def __init__(self,name,brand,price):
        
        self.name=name
        
        self.brand=brand
        
        self.price=price
        
    def __str__(self):
        
        return self.name
    
    
class showroom:
        
        name:str
        
        place:str
        
        
        def __init__(self,name,place):
        
            self.name=name
        
            self.place=place
        
            self.bikes=[]
        
        def add_vehicles(self,bike):
        
            self.bikes.append(bike)
        
        def list_vehicles(self):
        
            for b in self.bikes:
            
                print(b)
            

hunter_instance=bike("hunter","re",100000)
GT_instance=bike("GT","re",100000)
interceptor_instance=bike("interceptor","re",100000)
dominar_instance=bike("dominar400","re",100000)

showroom_instance=showroom("popular","kakkanad")

showroom_instance.add_vehicles(hunter_instance)

showroom_instance.add_vehicles(dominar_instance)

showroom_instance.list_vehicles()

showroom_instance2=showroom("tags","thrissur")

showroom_instance2.add_vehicles(hunter_instance)

showroom_instance2.add_vehicles(dominar_instance)

showroom_instance2.add_vehicles(GT_instance)

showroom_instance2.list_vehicles()



