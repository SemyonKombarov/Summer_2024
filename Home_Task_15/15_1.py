# dct = {1:1,2:2,3:{2:22,3:{1:111,2:222,3:{0:1111,1:2222,2:3333}},1:11},6:22}
dct = {1:{1:{1:11}}}
for i in dct:
    print(type(dct[i]))
def f(dct,x):
    res = []
    for i in dct:
        if int(i) == x:
            res.append(dct[i])
        if type(dct[i]) == dict:
            res.extend(f(dct[i],x))
    return res
print(*f(dct,1))