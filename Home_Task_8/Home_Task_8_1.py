a = "А"
g = "Г"
c = "Ц"
t = "Т"
n = list(input("Введите строку генетического кода ").upper())
lst = []
for i in range(len(n)):
    if i == 0:
        lst.append(n[i])
    if i >= 1:
        if lst[-1] == a and n[i] == g:
            lst[-1] = g
            lst.append(n[i])
        elif lst[-1] == g and n[i] == a:
            lst[-1] = a
            lst.append(n[i])
        elif lst[-1] == t and n[i] == c:
            lst[-1] = t
            lst.append(a)
            lst.append(g)
            lst.append(c)
        elif lst[-1] == c and n[i] == t:
            lst[-1] = c
            lst.append(a)
            lst.append(g)
            lst.append(t)
        else:
            lst.append(n[i])

print("Результат корректировки кода ",*lst)



