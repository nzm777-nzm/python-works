

class grandparent:
    
    def m1(self):
        
        print("grandparent m1 method")
        
class parent(grandparent):
    
    def m2(self):
        
        print("parent m2 method")


class child(parent):
    
    def m3(self):
        
        print("child m3 method")
        
child_instance=child()

child_instance.m3()

child_instance.m1()

child_instance.m2()