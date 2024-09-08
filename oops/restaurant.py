

class dishes:
    
    name:str
    
    price:int
    
    qty:int
    
    def __init__(self,name,price,qty):
        
        self.name=name
        
        self.price=price
        
        self.qty=qty
        
    def __str__(self):
        
        return self.name
    
    
class restuarant:
    
    name:str
    
    place:str
    
    
    def __init__(self,name,place):
        
        self.name=name
        
        self.place=place
        
        self.dish=[]
        
    def add_foods(self,dishes):
        
        self.dish.append(dishes)
        
    def list_dishes(self):
        
        for b in self.dish:
            
            print(b)
    

spanish_instance=dishes("spanish",1000,2)

french_instance=dishes("french",1000,1)

mexican_instance=dishes("mexican",2000,2)

turkish_instance=dishes("turkish",3000,1)


restuarant_instance=restuarant("spanish restaurant","barcelona")

restuarant_instance.add_foods(french_instance)

restuarant_instance.add_foods(spanish_instance)

restuarant_instance.list_dishes()

restuarant_instance2=restuarant("french","paris")

restuarant_instance2.add_foods(turkish_instance)

restuarant_instance2.add_foods(mexican_instance)

restuarant_instance2.add_foods(french_instance)

restuarant_instance2.add_foods(spanish_instance)

restuarant_instance2.list_dishes()

