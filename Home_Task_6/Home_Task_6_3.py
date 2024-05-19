import string
n = input("Введите строку состояющую из латинских букв, цифр или прочих знаков пунктуации ")

n1 = set(list(n))
#print(n,n1)
mn1 = string.ascii_lowercase
mn2 = string.digits
mn3 = string.punctuation
lst1 = set()
lst2 = set()
lst3 = set()
for i in n:
    if i in mn1:
        lst1.add(i)
for i in n:
    if i in mn2:
        lst2.add(i)
for i in n:
    if i in mn3:
        lst3.add(i)
print(*lst1)
print(*lst2)
print(*lst3)
# print(mn1,mn2,mn3)
