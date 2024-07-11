n = [5,4,3,2,1]
count = 0
for k,v in enumerate(n):
    for j,i in enumerate(n):
        if v != i and v < i:
            if  k > j:
                count += 1

print(f'Для списка {n} количество инверсий',count, 'штук')