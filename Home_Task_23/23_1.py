n = "aabbccddcc"
lst = []

z_max = ""

for i in n:
    lst.append(i)
for i in range(len(lst)):
    for j in range(len(lst)):
        z = "".join(lst[i:j+1])
        if z == z[::-1]:
            if len(z_max) < len(z):
                z_max = z
                

print(f"Длина подстроки с наибольшим палиндромом для заданной строки {n} является {len(z_max)} (подстрока '{z_max}')")





