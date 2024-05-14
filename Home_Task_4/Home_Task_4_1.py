s = input('Введите выражение: ').split()
a = float(s[0])
b = float(s[2])
z = s[1]
print("Результат:")
if z == "/" and b == 0:
    print("На ноль делить нельзя!")
elif z == "+":
    print(a + b)
elif z == "-":
    print(a - b)
elif z == "*":
    print(a * b)
elif z == "/" and b != 0:
    print(a / b)
