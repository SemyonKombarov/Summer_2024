class Inf:
    def __init__(self):
        self.number = 0
        self.counter = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.number += 1
        self.counter += 1
        if self.number > 26:
            self.number = 1
        if self.number % 2:
            return self.number
        else:
            return self.number

x = 60
f = Inf()
dct = {}
for i in range(int(x)):
    z = next(f)
    print(z,end = "")
    print(chr(z+64), end = " ")
    dct[z]=dct.get(z,chr(z+64))