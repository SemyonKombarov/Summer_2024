x = float(input("Введите число №1 для переменной х "))
y = float(input("Введите число №2 для переменной у "))
summa = x + y
print(f"Сумма {x=} и {y=} равна {summa}")
substraction = x - y
print(f"Разница между {x=} и {y=} равна {substraction}")
multiplication = x * y
print(f"Произведение {x=} и {y=} равно {multiplication}")
#Проверка условия деления на нуль
if y==0:
    print(f"Выражение = {x} / {y} пайтон считать не хочет, попробуйте дрпугие значения при запуске программы")
    # Поиск наибольшего среди 3-x значений, добавляю короткие переменные для удобства
    x1 = summa
    x2 = substraction
    x3 = multiplication
    # Проверка условия, что выбранные значения не равны между собой
    if x1 == x2 or x1 == x3 or x2 == x3:
    # Наибольшое число при одинаковых результатах расчёта
        if x1 == x2 and x1 > x3:
            print()
            print(f"Наибольшое значение {x1}")
        elif x1 == x3 and x1 > x2:
            print()
            print(f"Наибольшое значение {x3}")
        elif x2 == x3 and x2 > x1:
            print()
            print(f"Наибольшое значение {x2}")
        elif x1 == x2 and x1 < x3:
            print()
            print(f"Наибольшое значение {x3}")
        elif x1 == x3 and x1 < x2:
            print()
            print(f"Наибольшое значение {x2}")
        elif x2 == x3 and x2 < x1:
            print()
            print(f"Наибольшое значение {x1}")


    else:
        if x1 > x2 > x3 or x1 > x3 > x2:
            print()
            print("Наибольшее значение =", x1)
        elif x2 > x3 > x1 or x2 > x3 > x1:
            print()
            print("Наибольшее значение =", x2)
        elif x3 > x2 > x1 or x3 > x1 > x1:
            print()
            print("Наибольшее значение =", x3)
else:
    division = x / y
    integer_dision = x // y
    print(f"Деление {x=} на {y=} равна {division}")
    print(f"Целочисленное деление {x=} на {y=} равно {integer_dision}")
    # Поиск наибольшего среди 5-ти значений, добавляю короткие переменные для удобства
    x1 = summa
    x2 = substraction
    x3 = multiplication
    x4 = division
    x5 = integer_dision
    # В случае если нет одинаковых значений
    if x1 > x2 and x1 > x3 and x1 > x4 and x1 > x5:
        print()
        print(f"Наибольшое значение {x1}")
    elif x2 > x1 and x2 > x3 and x2 > x4 and x2 > x5:
        print()
        print(f"Наибольшое значение {x2}")
    elif x3 > x1 and x3 > x2 and x3 > x4 and x3 > x5:
        print()
        print(f"Наибольшое значение {x3}")
    elif x4 > x1 and x4 > x2 and x4 > x3 and x4 > x5:
        print()
        print(f"Наибольшое значение {x4}")
    elif x5 > x1 and x5 > x2 and x5 > x3 and x5 > x4:
        print()
        print(f"Наибольшое значение {x5}")
    else:
        #Если вдруг какие-то значения дублируются
        if x1 == x2 or x1 == x3 or x1 == x4 or x1 == x5 or x2 == x3 or x2 == x4 or x2 == x5 or x3 == x4 or x3 == x5 or x4 == x5:
            if x1 == x2 and x1 >= x3 and x1 >= x4 and x1 >= x5:
                print()
                print(f"Наибольшое значение {x1}")
            elif x1 == x3 and x1 >= x2 and x1 >= x4 and x1 >= x5:
                print()
                print(f"Наибольшое значение {x1}")
            elif x1 == x4 and x1 >= x2 and x1 >= x3 and x1 >= x5:
                print()
                print(f"Наибольшое значение {x1}")
            elif x1 == x5 and x1 >= x2 and x1 >= x3 and x1 >= x4:
                print()
                print(f"Наибольшое значение {x1}")
            elif x2 == x3 and x2 >= x1 and x2 >= x3 and x2 >= x4:
                print()
                print(f"Наибольшое значение {x2}")
            elif x2 == x4 and x2 >= x1 and x2 >= x3 and x2 >= x3:
                print()
                print(f"Наибольшое значение {x2}")
            elif x2 == x5 and x2 >= x1 and x2 >= x3 and x2 >= x4:
                print()
                print(f"Наибольшое значение {x2}")
            elif x3 == x4 and x3 >= x1 and x3 >= x2 and x3 >= x4:
                print()
                print(f"Наибольшое значение {x3}")
            elif x3 == x5 and x3 >= x1 and x3 >= x2 and x3 >= x4:
                print()
                print(f"Наибольшое значение {x3}")
            elif x4 == x5 and x4 >= x1 and x4 >= x2 and x4 >= x3:
                print()
                print(f"Наибольшое значение {x4}")






