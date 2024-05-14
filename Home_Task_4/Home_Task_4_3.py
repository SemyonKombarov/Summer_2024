pred1 = input("Введите первое предложение ")
pred2 = input("Введите второе предложение ")
s1 = pred1.lower()
s2 = pred2.lower()
dct1 = {}
dct2 = {}
for i in s1:
    if i not in " ,.:;?!/|0123456789@":
        if i not in dct1: dct1[i] = 1
        else: dct1[i] += 1
for k in s2:
    if k not in " ,.:;?!/|0123456789@":
        if k not in dct2: dct2[k] = 1
        else: dct2[k] += 1
#print(dct1,dct2)
print("Предлоджения анаграммы?",dct1 == dct2)