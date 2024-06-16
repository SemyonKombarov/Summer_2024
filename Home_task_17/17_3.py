class Shape:
    def __init__(self,name,colour,square):
        self.name = name
        self.colour = colour
        self.square = square
    def set_colour(self):
        self.colour = input("Установаите цвет фигуры ")
    def info_colour(self):
        print(self.colour)
    def set_square(self):
        self.square = int(input("Установите площадь фигуры "))
    def info_square(self):
        print(self.square)
    def info_shape(self):
        print(f"{self.name} {self.colour} {self.square}")

shape1 = Shape("Shape1","black",4)
shape1.info_shape()
shape1.set_colour()
shape1.set_square()
shape1.info_shape()


