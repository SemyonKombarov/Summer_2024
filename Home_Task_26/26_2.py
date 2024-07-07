# class Pet_example:
#     def __init__(self, name,age,year,type):
#         self.name = name
#         self.age = age
#         self.year = year
#         self.type = type

def dis(self):
    for i in self.__dict__:
        print(i, getattr(self,i,None))

Pet = type('Pet',(),{'dis':dis})
my_pet = Pet()
my_pet.name = "Tom"
my_pet.age = 10
my_pet.profession = "cat"
# print([items for items in Pet.__dict__])
dis(my_pet)

