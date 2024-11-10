


from abc import ABC,abstractmethod

class car(ABC):
    
    @abstractmethod
    def start(self):
        print("car is started")
        
    @abstractmethod    
    def accelerate(self):
        print("car is accelerated")
        
    @abstractmethod    
    def stop(self):
        print("car is stopped")
        
class thar(car):
    
    def start(self):
        
        print("thar is started")
        
    def accelerate(self):
        
        print("thar is accelerate")
        
    def stop(self):
        
        print("thar is stopped")
        

class fortuner(thar):
    
    def start(self):
        
        print("fortuner started")
        
    def accelerate(self):
        
        print("fortuner accelerated")
        
    def stop(self):
        
        print("fortuner stopped")
        
        
class innova(fortuner):
    
    def start(self):
        
        print("innova is started")
        
    def accelerate(self):
        
        print("innova is accelerate")
        
    def stop(self):
        
        print("innova is stopped")
        

vehicle=fortuner()

vehicle.accelerate()

vehicle2=innova()

vehicle2.start()

vehicle2.stop()

vehicle3=thar()

vehicle3.stop()

        
        

    
    
    
    
        
        