f_in = open("text1.txt", encoding="utf-8")
lst = []
for i in f_in:
    j = i.split()
    k = j[::-1]
    lst.append(k)
g = lst[::-1]
f_in.close()

f_out = open("text2.txt","w", encoding = "utf-8")
for i in g:
    f_out.write(" ".join(i)+"\n")
f_out.close()