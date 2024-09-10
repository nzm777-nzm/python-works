

class operations:
    
    def perform_add(self,*args):
        
        total=sum([arg for arg in args if isinstance(arg,(int,float))])
        
        return total
        
    def get_max_numbers(self,*args):
        
        return max(args)
    

math=operations()

print(math.perform_add(10,20))

print(math.perform_add(10,20,30))

print(math.perform_add(10,20,30,30.5,"hai"))