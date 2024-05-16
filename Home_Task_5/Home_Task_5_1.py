# n = int(input()) #Глубина пирамиды
# lst = []
# for i in range(n):
#     stroka = [1] * (i+1)
#     for j in range(i+1):
#         if j != 0 and j!= i:
#             stroka[j] = lst[i-1][j-1] + lst[i-1][j]
#             print(stroka)
#     lst.append(stroka)
# for _ in lst:
#     print(_)


n = int(input())
dct ={}
for i in range(1,n+1):
    dct[i]=dct.get(i,1)
    for j in dct:
        # print(j)
        if j != 1 and j != i:
            dct[j] = dct[i-1] + dct[i]
    print(dct.values())