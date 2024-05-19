n = list(input("Введите значение латинскими буквами ").upper())
#n = ["M","M","M","L","C","I"]
#print(n)
lst = []
dct = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
for i in n:
    lst.append(dct[i])
#print(lst)
lst1 = []
for i in range(len(lst)):
    # if (i == len(lst)): break
    x = lst[-1]
    if lst[i-1] < lst[i] and lst[i-1] != x:
        lst1.pop(i-1)
        y = lst[i] - lst[i-1]
        lst1.append(y)
        #print(i,lst[i-1], lst[i])
    else:
        lst1.append(lst[i])
        #print(lst1)
#print(lst1)
z = 0
for i in lst1:
    z = z + i
print(z)



