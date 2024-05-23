n = ['abab','xx','aaaaaaa','abcbab']
#----------------------------------------#
abc = "abcdefghijklmnopqrstuvwxyz"
lst_abc = list(abc)
dct = {}
for i in range(len(lst_abc)):
    dct[lst_abc[i]]=dct.get(lst_abc[i],i+1)
tes_abc = set(abc)
dct1 = {}
dct_alf = {}
for i in n:
    tes = set()
    for j in i:
        if j in tes_abc:
            tes.add(j)
    if len(tes) == 1:
        dct_alf[i]=dct_alf.get(i,dct[j])
    else:
        dct1[i]=dct1.get(i,len(tes))

d1 = sorted(dct1.items(), key=lambda x: x[1], reverse=True)
d2 = sorted(dct_alf.items(), key=lambda x: x[1])
d1.extend(d2)
# print(d1)
for i in d1:
    print(i[0], end=" ")
# print(sorted(dct1.items(), key=lambda x: x[1], reverse=True), sorted(dct_alf.items(), key=lambda x: x[1]))
# print(sorted(dct.items(), key = lambda x:x[1], reverse= True))