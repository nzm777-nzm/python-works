

# from abc import ABC,abstractmethod

# class bank(ABC):


class bank:
    
    acno:int
    
    bank_name:str
    
    balance:int
    
    ac_type:str
    
    def create_account(self,acno,ac_type):
        
        self.bank_name="SBT"
        
        self.__balance=2000
        
        self.acno=acno
        
        self.ac_type=ac_type
        
    def deposit(self,amount):
        
        self.__balance+=amount
        
        print(f"your {self.bank_name} ACC with {self.acno} has been credited with amount{amount} avilable balance{self.__balance}")
        
    def withdraw(self,amount):
        
        if amount>self.__balance:
            
            print("transaction failed insufficient balance")
            
        else:
            
            self.__balance-=amount
            
            print(f"your {self.bank_name} ACC with {self.acno} has been credited with amount{amount} available balance{self.__balance}")
            
    def get_balance(self):
        
        print(f"aval balance={self.__balance}")
        
user_account=bank()

user_account.create_account(1,"savings")

user_account.withdraw(1000)

user_account.deposit(5000)

user_account.get_balance()






        
    
        
        
            



        


    
    
    
    
    