def code(n,m):
    abc = "abcdefghijklmnopqrstuvwxyz"
    lst_abc = list(abc)
    tes_abc = set(lst_abc)
    dct = {}
    dct_d = {}
    for i in range(len(lst_abc)):
        dct[lst_abc[i]] = dct.get(lst_abc[i], i + 1)
        dct_d[i + 1] = dct_d.get((i + 1), lst_abc[i])

    for i in n:
        if i in tes_abc:
            if dct[i] + m >= 27:
                print(dct_d[dct[i] + m - 26], end="")
            else:
                print(dct_d[dct[i] + m], end="")
                continue
        else:
            print(i, end="")

n = str(input("Введите строку "))
m = int(input("Введите ключ шифрования "))
print(code(n,m))


