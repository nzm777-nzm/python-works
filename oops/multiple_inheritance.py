

class grandparent:
    
    def m1(self):
        
        print("grand m1")
        
class parent:
    
    def m2(self):
        
        print("parent m2")

class child(parent,grandparent):
    
    def m3(self):
        
        print("child m3 method")
    

child_instance=child()

child_instance.m1()

child_instance.m2()

child_instance.m3()