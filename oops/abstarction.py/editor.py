
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
    
    
    