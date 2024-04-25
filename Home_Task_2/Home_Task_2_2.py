#Решил задать числа через функцию random
import random
print("Программа генерирует список состоящих из 3х псевдослучайных челых чисел в диапазоне от -10 до 10")
print()
lst = [random.randint(-10,10),random.randint(-10,10),random.randint(-10,10)]
lst1 = lst[:]
print(f"Рассматриваемый список {lst1}")
print()
a, b, c = lst1[0], lst1[1],lst1[2]
#print(a,b,c)
mnmm = 0
print("Результаты через применение оператора if")
#Подход к решению задачи аналогичен ДЗ_1_2
if a < mnmm and a != mnmm:
    mnmm = a
if b < mnmm:
    mnmm = b
if c < mnmm:
    mnmm = c
print(f"Минимальное значение из списка равно {mnmm}")
maxx = 0
if a > maxx and a != maxx:
    maxx = a
if b > maxx:
    maxx = b
if c > maxx:
    maxx = c
print(f"Минимальное значение из списка равно {maxx}")
print()
print("Результаты через применение функции sort,min,max для сравнения")
lst1.sort()
print(f"Минимальное значение из списка равно {min(lst1)}")
print(f"Максимальное значение из списка равно {max(lst1)}")
print()
