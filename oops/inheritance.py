

class vehicle:
    
    def start(self):
        
        print("vehicle is started")
        
    def accelerate(self):
        
        print("vehicle accelerate method")
        
class swift(vehicle):
    
    pass

swift_inheritance=swift()

swift_inheritance.accelerate()

swift_inheritance.start()