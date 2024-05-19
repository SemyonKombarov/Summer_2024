n1 = set(input("Книги первого читателя: ").split(", "))
n2 = set(input("Книги второго читателя: ").split(", "))
lst = []
for i in n1:
    for j in n2:
        if i == j:
            lst.append(i)
        #print(i,j)
print("Количество книг которые прочитали оба читателя = ", len(n1.intersection(n2)), " рассчитано через intersection")
print("Количество книг которые прочитали оба читателя = ", len(lst)," рассчитано через цикл")