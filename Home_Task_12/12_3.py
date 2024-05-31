n = "1-2,4-4,3-6"
def fun(n):
    n = n.split(",")
    print(n)
    lst = []
    for i in n:
        m1 = i.split("-")[0]
        m2 = i.split("-")[1]
        if m1 != m2:
            x = [lst.append(i) for i in range(int(m1),int(m2)+1)]
        else:
            lst.append(int(m1))
    return lst
print(fun(n))