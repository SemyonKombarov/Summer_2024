import copy

n = int(input("Введите число для определения делителя "))
lst = []
for i in range(1,n+1):
    x = n % i
    if x == 0:
        lst.append(i)
print("Первая часть задания",*lst)
print()
print("Вторая часть задания без форматирования")
lst1 = []
lstk = []
lsti = []
for i in range(n+1):
    for k in lst:
        if k**i <= n and k**i != 1 and k**i != 0:
            lst1.append(k**i)
            lstk.append(k)
            lsti.append(i)
# print(lstk,lsti)
# print(lst1)
lst2 = copy.copy(lst1)
# print(lst2)

print()
for j,g in enumerate(lst1):
    for p, f in enumerate(lst2):
        y = g * f
        if y == n:
            # print(f"Произведение {g} и {f} с индексами {j} и {p}")
            # print(lst1[j],lst2[p])
            print(f"({lstk[j]} ** {lsti[j]}) * ({lstk[p]} ** {lsti[p]}) = {n}")




# lst1 = [k for k in lst]
# lst2 = [k*1 for k in lst]
# lst3 = []
# # print(lst1, lst2)
# for j in lst1:
#     for p in lst2:
#         y = j * p
#         if y == n:
#             print(y,j,p)

