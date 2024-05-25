# n = list(input("Введите генетический код ДНК"))
n = "GGTCAA"
print(n)
lst = []
for i in n:
    if i == "G":
        lst.append("C")
    elif i == "C":
        lst.append("G")
    elif i == "T":
        lst.append("A")
    elif i == "A":
        lst.append("A")
print("Решение через цикл","".join(lst))



