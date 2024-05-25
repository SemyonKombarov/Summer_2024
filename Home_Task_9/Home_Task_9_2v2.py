n = "питон"
n_lst = "поросенок, титан, итог, лавка, погост, кино"

def count(n):
    n = list(n)
    lst_words = []
    x = 0
    for i in n:
        if i in "ауоыиэяюёе":
            lst_words.append(n.index(i,x))
        x = x + 1
    return lst_words

lst = []
dct1 = count(n)
n_lst = n_lst.split(", ")
for i, j in enumerate(n_lst):
    if count(j) == dct1:
        lst.append(j)
print(f"Похожие слова на {n} это: \n{", ".join(lst)}")