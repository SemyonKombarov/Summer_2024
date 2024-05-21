n = [4, 6]
# mx = n[0]*n[1]
# lst = []
# for j in range(mx):
#     x = mx - j
#     lst.append(x)
# print(lst)
# #print(sorted(lst))
# lst_minimum = []
# for i in lst:
#     y1 = i % n[0]
#     y2 = i % n[1]
#     if y1 == 0 and y2 == 0:
#         lst_minimum.append(i)
# print(min(lst_minimum))

def nok(x):
    maximum = 1
    lst =[]
    lst.extend(x)
    #print(lst)
    lst1 = []
    for i in x:
        maximum = maximum * i
        #print(x,maximum)
    for j in range(maximum):
        x = maximum - j
        lst1.append(x)
    #print("lst1 ",lst1)
    # lst2 = sorted(lst1)
    # print("lst2 ",lst2)
    dct = {}
    lst_minimum = []
    for p in lst1:
        for i in lst:
            y = p % i
            #print(p, i, y)
            if y == 0:
                dct[p]=dct.get(p,0)+1
    #print(dct)
    for i in dct:
        if dct[i] == len(lst):
            lst_minimum.append(i)
    print("Наименьшее общее кратное чисел", *lst,"это",min(lst_minimum))

nok(n)

