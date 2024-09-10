

from abc import ABC,abstractmethod

class car(ABC):
    
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def accelerate(self):
        pass
    @abstractmethod
    def stop(self):
        pass
    
class swift(car):
    
    def start(self):
        
        print("car is started")
        
    def accelerate(self):
        
        print("car is accelarate")
        
    def stop(self):
        
        print("car is stopped")
        
vehicle=swift()

vehicle.start()

vehicle.stop()

vehicle.accelerate()
    
    