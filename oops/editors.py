

class editor:
    
      def __init__(self,name,vendor):
          
         self.name=name
         
         self.vendor=vendor
         
      def open(self):
             
            print(f"{self.name} open editor")
            
      def execute(self):
          
            print(f"{self.name} execute")
                   
class vscode(editor):
    
    def __init__(self,name,vendor):
        
         super().__init__(name,vendor)   
         

class pyCharm(editor):
    
    def __init__(self,name,vendor):
        
        super().__init__(name,vendor)      


vscode_inheritance=vscode("vscode","vscvendor")

vscode_inheritance.open()

pycharm_instance=pyCharm("pycharm","jetbrains")

pycharm_instance.execute()
