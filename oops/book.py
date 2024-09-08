
class book:
    
    tittle:str 
    
    author:str
    
    price:int
    
    language:str
    
    
    def __init__(self,title,author,price,language): # to initialize instance variable => constructor
        
        self.tittle=title
        
        self.author=author
        
        self.price=price
        
        self.language=language
        
    def display_book(self):
        
        print(self.tittle,self.author,self.price,self.language)
        
    def __str__(self): #object string representation
        
        return self.tittle    
        
book_instance1=book("poem","shakespear",1000,"english")

book_instance2=book("suii","ronaldo",1000000,"portugese")

book_instance1.display_book()

book_instance2.display_book()

print(book_instance1)
        
        