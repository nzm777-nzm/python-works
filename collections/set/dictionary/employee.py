
employee={"name":"nzm","dept":"r&d","salary":50000,"combo_offer":1000,"extra_workdays":2}

for k,v in employee.items():
    
    print(k,v)
    
if "extra_workdays" in employee:
        
    net=employee.get("salary")+employee.get("combo_offer")*employee.get("extra_workdays")
        
    print(net)
        
else:
    
    net=employee.get("salary")
    
    print(net)
   
    
    