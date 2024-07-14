n1 = "abc"
n2 = 'xyz'
count = 0
if len(n1) == len(n2):
    for k1,v1 in enumerate(list(n1)):
        for k2, v2 in enumerate(list(n2)):
            if k1 == k2 and v1 == v2:
                continue
            elif k1 == k2 and v1 != v2:
                count += 1
    print(f'{n1} и {n2} - {count}')
else:
    print('Количество элементов в строках не совпадает')

