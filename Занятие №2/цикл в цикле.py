lst = [10,20,30,40,50]
res = []
s = 0
#Перебор значений из цикла
for i in lst:
    s += i
    res.append(s)
print(res)

print(60 in res)
print(70 in res)

print(res + lst)

lst=[[1,2,3],[10,20],[100,200,300,400]]
su = 0
for x in lst:
    print(x)
    for y in x:
        su =su + y
        print(su)
print(su)