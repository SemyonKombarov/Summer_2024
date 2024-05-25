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
def zamena(i):
    if i == "G":
        j = "C"
    elif i == "C":
        j = "G"
    elif i == "T":
        j = "A"
    elif i == "A":
        j = "A"
    return j

print("Решение через функцию", end=" ")
for i in n:
    print(zamena(i), end="")




