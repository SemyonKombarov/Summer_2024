n1 = "abc"
n2 = "acb"

lst1 = []
lst2 = []
lst = []

#Разбиваем строки n1 и n2 на 2 списка для последующей проверки условий
for i in n1:
    lst1.append(i)
for i in n2:
    lst2.append(i)

#Условие что строки полностью равны
if n1 == n2:
    print(True)
else:
    #Условие что сроки имеют одинаковую протяженность
    if len(lst1) == len(lst2):
        for i in range(len(lst1)):
            if lst1[i] == lst2[i]:
                lst.append(1)
            else:
                lst.append(0)
        if sum(lst) == len(lst) - 1:
            print(True)
        else:
            print(False)
    #Условие что строка одного больше другого на 1 значение:
    else:
        if len(lst1) - len(lst2) > 1 or len(lst2) - len(lst1) > 1:
            print(False)
        else:
            # Условие если протяженность первой строки короче второй
            if len(lst1) < len(lst2):
            #Условие что первое значение из списка lst1 равно первому значению из спиcка lst2, проверка идёт сначала строки
                if lst1[0] == lst2[0]:
                    for i in range(len(lst1)):
                        if lst1[i] == lst2[i]:
                            lst.append(1)
                        else:
                            lst.append(0)
                    if sum(lst) == len(lst1):
                        print(True)
                    else:
                        print(False)
                # Проверка идёт с конца строки
                elif lst1[-1] == lst2[-1]:
                    for i in range(len(lst1)):
                        if lst1[i] == lst2[i+1]:
                            lst.append(1)
                        else:
                            lst.append(0)
                    if sum(lst) == len(lst1):
                        print(True)
                    else:
                        print(False)

                else:
                    print(False)

            else:
                # Условие если протяженность второй строки короче первой
                if lst1[0] == lst2[0]:
                    for i in range(len(lst2)):
                        if lst1[i+1] == lst2[i]:
                            lst.append(1)
                        else:
                            lst.append(0)
                    if sum(lst) == len(lst2):
                        print(True)
                    else:
                        print(False)
                elif lst1[-1] == lst2[-1]:
                    for i in range(len(lst2)):
                        if lst1[i+1] == lst2[i]:
                            lst.append(1)
                        else:
                            lst.append(0)
                    if sum(lst) == len(lst2):
                        print(True)
                    else:
                        print(False)
                else:
                    print(False)



