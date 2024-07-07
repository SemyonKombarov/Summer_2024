class Person:
    def __init__(self, name,age):
        self.name = name.title()
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def set_age(self, new_age):
        if 1 < new_age < 100:
            self._age = new_age
        else:
            print("Недопустимый возраст")



tom = Person('Tom',10)
print(getattr(tom,'age'))

