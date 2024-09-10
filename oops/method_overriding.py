

class parent:
    
    def bike(self):
        
        print("passon pro")
        
    def mobile(self):
        
        print("samsung s20")
        
class child(parent):
    
    def bike(self):
        
        print("GT")
        
    def mobile(self):
        
        print("iphone 15")

child_instance=child()

child_instance.bike()

child_instance.mobile()