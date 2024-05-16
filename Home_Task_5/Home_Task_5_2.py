
n = int(input("Введите число для определения делителя "))
lst = []
for i in range(1,n+1):
    x = n % i
    if x == 0:
        lst.append(i)
print("Первая часть задания",*lst)
print()
print("Вторую часть пока что не придумал как реализовать...")
# lst1 = [k for k in lst]
# lst2 = [k*1 for k in lst]
# lst3 = []
# # print(lst1, lst2)
# for j in lst1:
#     for p in lst2:
#         y = j * p
#         if y == n:
#             print(y,j,p)

