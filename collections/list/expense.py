expenses=[12000,13000,11000,14000,15000,21000,22000,13000]

total=0

expense_count=len(expenses)

for i in range(0,len(expenses)):
    
    # if expenses[i] > 15000:
    
        total=total+expenses[i]
        
        avg=total/len(expenses)
        
print(f"total={total} avg={avg}")

         
    
    