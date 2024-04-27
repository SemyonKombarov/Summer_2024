n = input("Введите предложение ")
#n = 'Я люблю Питон и кофе '
x = n.split()
max1 = 0
max2 = 0
maximum = []
lst = []
for k, j in enumerate(x):
    if len(j) > max1:
        max1 = len(j)
        maxi = j
        max2 = k
        #print(maxi)
    lst.append(len(j))
    if len(maxi) == len(j):
        maximum.append(j)

print(f"Первое наибольшее слово в предложении -{n}- это '", maxi, "'")
print(f'Список со всеми самыми длинными словами по порядку {maximum}')

        #print("max", max1, max2)

