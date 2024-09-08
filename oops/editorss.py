

class editor:
    
    def __init__(self,name,vendor):
        
        self.name=name
        
        self.vendor=vendor
        
    def open(self):
        
        print(f"{self.name} open ")
        
    def execute(self):
        
        print(f"{self.name} execute")
        
    def closed(self):
        
        print(f"{self.vendor} stopped proccess")
        
class vscode(editor):
    
    def __init__(self,name,vendor):
        
        super().__init__(name,vendor)
        
class pyCharm(editor):
    
    def __init__(self,name,vendor):
        
        super().__init__(name,vendor)
        
vscode_instance=vscode("vscode","vscvendor")

vscode_instance.open()

vscode_instance.execute()

vscode_instance.closed()

pyCharm_instance=pyCharm("pycharm","jetbrains")

pyCharm_instance.closed()

pyCharm_instance.execute()

pyCharm_instance.open()