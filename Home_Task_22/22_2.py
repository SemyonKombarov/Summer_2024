n = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (6, 7), (7, 8)]

# Функция по определению конечных/начальных точек древа
def rec(n):
    tes = set()
    for i in n:
        for j in i:
            tes.add(j)
    lst_of_starts1 = []
    lst_of_starts2 = []
    for m in tes:
        for i in n:
            if i[0] == m:
                lst_of_starts1.append(m)
            if i[1] == m:
                lst_of_starts2.append(m)
    lst_of_ends_a =[]
    lst_of_ends_b = []
    for i in tes:
        if i not in lst_of_starts1:
            lst_of_ends_a.append(i)
        elif i not in lst_of_starts2:
            lst_of_ends_b.append(i)

    return lst_of_ends_a,lst_of_ends_b

z = rec(n)
print("z", z[0],z[1])
na4alo = z[1] # Корень древа
konec = z[0] # Вершины - все возможные

lst = []

def poisk(m,n):

    for i in n:
        if i[1] == m:
            print(i)
            print(m)
            z = i[0]
            m = i
            poisk(z,n)



# x = poisk(8,n)
# print(x)

for i in konec:
    print(f"Путь из вершины {i} до корня {na4alo}")
    poisk(i,n)
    print(1)
    print()
