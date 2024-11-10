
from abc import ABC,abstractmethod

class editor(ABC):
    
    @abstractmethod
    def open(self):
        
        pass
    @abstractmethod
    def execute(self):
        
        pass
    @abstractmethod
    def debug(self):
        
        pass
    
class vscode(editor):
    
    
    def open(self):
        
        print("opened")
        
    def execute(self):
        
        print("executed")
        
    def debug(self):
        
        print("debug")
        

vs_code=vscode()

vs_code.open()

vs_code.execute()

vs_code.debug()
    
   
  
    
    
    