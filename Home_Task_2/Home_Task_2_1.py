n = input("Введите число для формирования таблицы умножения ")
print()
print(f"Таблица умножения для числа {n}:")
for i in range(1,10):
    y = i*int(n)
    print(f"{i} x {n} = {y}")