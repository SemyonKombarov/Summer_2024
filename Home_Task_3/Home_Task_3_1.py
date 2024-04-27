summa = 0
p = -1
while True:
    p = p + 1
    x = p + 1
    print(f"Введите зарплату {x} сотрудника, для выхода из расчёта ввёдите 0")
    n = int(input())
    if n == 0:
        break
    else:
        summa = summa + n
if p == 0:
    print("Выход из программы")
else:
    sred = summa / p
    print(f"Среднее арифметическое значение заработной платы {p} введённых сотрудников равна {sred} у.е.")
