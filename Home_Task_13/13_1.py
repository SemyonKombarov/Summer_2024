def fun():
    i = 1
    while True:
        for _ in range(i):
            if i % 2:
                yield i
                i += 1
            else:
                yield -1 * i
                i += 1

g = fun()
for i in range(100):
    print(next(g), end=" ")