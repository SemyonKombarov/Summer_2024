lst = [1,2,3, 5, 99,-12]
# lst = list(map(int, input().split()))
# s = input (
mi = lst[0] # mi = float("inf")
# print(lst)

for i in lst:
    #print(i)
    #x = int(lst[i])
    if i < mi:
        mi = i
print(mi)


