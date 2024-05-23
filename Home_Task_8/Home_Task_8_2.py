import string

n = [[1,5,3],[2,44,1,4],[3,3]]
print(f"Введённая строка {n}")
lst = []
for i in n:
    r_sorted = sorted(i, reverse=True)
    x = r_sorted
    r = str(r_sorted)
    m = 0
    for p in r:
        if p in string.digits:
            m += 1
    lst.append([x,m])

y = sorted(lst, key= lambda x:x[1])
lst_final = []
for i in y:
    i.remove(i[1])
    lst_final.append(i[0])
print(f"Результат сортировки по заданию {lst_final}")


