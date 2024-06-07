def fun(n):
    if n !=1:
        print("*"*n)
    n-=1
    if n >= 1:
        fun(n)
    print("*"*(n+1))
    return
fun(10)