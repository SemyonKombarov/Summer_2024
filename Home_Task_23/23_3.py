from itertools import permutations
n = [9,81,25]
z = list(permutations(n,len(n)))
x_max = 0
lst = []
for i in z:
    for j in i:
        lst.append(str(j))
        if len(lst) == len(n):
            delimiter = ''
            x = delimiter.join(lst)
            lst = []
            if int(x) > x_max:
                x_max = int(x)

print(f"Самое большое число которое можно составить из списка {n} это {x_max}")


