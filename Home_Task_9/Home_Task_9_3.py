# n = input()
n = "Мама мыла раму"
dct = {}
for i in n.lower():
    dct[i]=dct.get(i,0)+1
res = sorted(dct.items(), key = lambda x: (-x[1],x[0]))
print(res)
if len(res) >= 10:
    for i in range(0,10):
        print(res[i][0], "-",res[i][1])
else:
    for i in res:
        print(i[0], "-",i[1])