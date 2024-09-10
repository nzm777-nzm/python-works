

def flat_list(*args):
    
  flat=[]
  
  for arg in args:
      
      if isinstance(arg,list):
          
          flat.extend(flat_list(*arg))
        
      else:
          
          flat.append(arg)

flat_list(1,2,[10,20],[10,[100,200]])



#expeceted_output=[1,2,10,20,10,100,200]