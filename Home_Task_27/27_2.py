class Item:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def total(self):
        return self.price * self.quantity

    def __getattribute__(self, attr):
        if attr == "name":
            x = object.__getattribute__(self, attr)
            return x.title()
        else:
            return object.__getattribute__(self, attr)

book = Item("book1",100,10)
cucumber = Item('cucumber',10,50)
print(book.name)
print(cucumber.name)
print(book.total())
print(cucumber.total())

