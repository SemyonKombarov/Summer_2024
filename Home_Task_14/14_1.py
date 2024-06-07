def fun(n):
    print("fun до", n)
    if n // 10 == 0:
        n = 0
        return n + 1
    else:
        return fun( n // 10 )



print(fun(4091))