class Cafe:
    def __init__(self,name):
        self.name = name
    ass = {}
    doxod = 0
    prodanie_tovari = {}
    posetiteli = 0
    def __str__(self):
        return f"Заведение {self.name}"
    def otchet(self):
        print("*"*20)
        print(f"Дневная выручка {Cafe.doxod}")
        print("*" * 20)
        print(f"Количество посетителей {Cafe.posetiteli}")
        print("*" * 20)
        print(f"Проданные товары {Cafe.prodanie_tovari}")



class Assortment:
    def __init__(self,name ,price):
        self.name = name
        self.price = price
        Cafe.ass[name] = Cafe.ass.get(name, price)
    def __str__(self):
        return f"Ассортимент {self.name}"

class Buyer:
    base = [] # Клиентская база
    loyal = {} # Программа лояльности
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        Buyer.base.append(self.name)
        Buyer.loyal[self.name]=Buyer.loyal.get(self.name,0)
    def __str__(self):
        return f"Покупатель {self.name}"
    def zakaz(self):
        self.zakaz = input('Добрый день, введите продукт для заказа ')
        if self.zakaz not in Cafe.ass:
            print("Такой позиции в меню нет")
        else:
            if self.balance < Cafe.ass[self.zakaz]:
                print("Недостаточно средств")
            else:
                self.balance = self.balance - Cafe.ass[self.zakaz]
                Cafe.doxod = Cafe.doxod + Cafe.ass[self.zakaz]
                Buyer.loyal[self.name]=Buyer.loyal[self.name] + Cafe.ass[self.zakaz]*0.5
                Cafe.posetiteli += 1
                Cafe.prodanie_tovari[self.zakaz]=Cafe.prodanie_tovari.get(self.zakaz,0) + 1




cafe = Cafe("Veslo")
print(cafe)
a = Buyer("Anna",100)
b = Buyer("Vasya",500)
print(a,b)
# print(Buyer.base)
# print(Buyer.loyal)
coffe = Assortment("Кофе",100)
tea = Assortment("Чай",200)
bulka = Assortment("Булка",50)
print(Cafe.ass)

a.zakaz()
# print(Cafe.doxod)
# print(a.balance)
# print(Buyer.loyal)

cafe.otchet()