class Item:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def total(self):
        return self.price * self.quantity

    def __getattr__(self, attr):
        x = object.__getattr__(self, attr)
        return x.title()

book = Item("book1",100,10)
cucumber = Item('cucumber',10,50)
print(book.name)
print(book.total())
print(cucumber.total())

