# creating a class for books in an library

class Book(object):
    def __init__(self,bookName,author,price):
        self.bookName = bookName
        self.author = author
        self.price = price
    
    def change_price(self,newPrice):
        self.price = newPrice
    
    def get_details(self):
        return f'{self.bookName} was written by {self.author} and it costs {self.price} Rs.'
    

book1 = Book('Origin of Species','Charles Drawin',60.0)
book2 = Book('Rough Note','Sudharsan','priceless')

print(book1.get_details())
print(book2.get_details())

book1.change_price(55.0)
print(book1.get_details())



        