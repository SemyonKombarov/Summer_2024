def code(n,m):
    abc = "abcdefghijklmnopqrstuvwxyz"
    lst_abc = list(abc)
    tes_abc = set(lst_abc)
    dct = {}
    dct_d = {}
    for i in range(len(lst_abc)):
        dct[lst_abc[i]] = dct.get(lst_abc[i], i)
        dct_d[i] = dct_d.get((i), lst_abc[i])
    # print(dct)
    # print(dct_d)
    for i in n:
        if i in tes_abc:
            if dct[i] + m <= 25:
                print(dct_d[dct[i]+m], end="")

            else:
                print((dct_d[(dct[i]+m)%26]), end="")

        else:
            print(i, end="")
    return ""
# n = "abcdefghijklmnopqrstuvwxyz z abcyxz"
# m = 1

n = str(input("Введите строку "))
m = int(input("Введите ключ шифрования "))
print(code(n,m))


