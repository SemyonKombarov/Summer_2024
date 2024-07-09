n = [1,2,3,[4,5,[6,7,[9,[]]]]]

def fun(n):
    count = 0
    for i in n:

        if isinstance(i, list):
            print(True)
            count += fun(i) + 1
        else:
            count += 1
    return count

print(fun(n))