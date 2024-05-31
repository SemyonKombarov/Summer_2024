n = input("Введите число ")
# n = "2024"
n1 = n[::-1]
# print(n1)
lst = []
for i, j in enumerate(n1):
    if int(j)*10**i != 0:
        lst.append(int(j)*10**i)
        lst1 = lst[::-1]

rim = []
for i in lst1:
    if i >= 1000:
        x = (int(i/1000)) * ("M")
        rim.append(x)
    elif i == 900:
        rim.append("CM")
    elif i < 900 and i > 500:
        rim.append("D"+int((i-500)/100)*"C")
    elif i == 500:
        rim.append("D")
    elif i == 400:
        rim.append("CD")
    elif i == 300:
        rim.append("CCC")
    elif i == 200:
        rim.append("CC")
    elif i == 100:
        rim.append("C")
    elif i == 90:
        rim.append("XC")
    elif i < 90 and i > 50:
        rim.append("L"+int((i-50)/10)*"X")
    elif i == 50:
        rim.append("L")
    elif i == 40:
        rim.append("XL")
    elif i == 30:
        rim.append("XXX")
    elif i == 20:
        rim.append("XX")
    elif i == 10:
        rim.append("X")
    elif i == 9:
        rim.append("IX")
    elif i < 9 and i > 4:
        rim.append("V"+int((i-5)/1)*"I")
    elif i == 5:
        rim.append("V")
    elif i == 4:
        rim.append("IV")
    else:
        rim.append("I"*int(i))
print("".join(rim))
# d = 10
# lst = []
# for i in range(1,len(n)+1):
#     x = int(n)%(d**i)
#     lst.append(x)
#     print(x)
# lst.append(int(n))
# for i in range(len(lst)):
#     x = 0



