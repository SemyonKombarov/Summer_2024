# n = int(input())
# dct = {}
# p = 0
# for i in range(2):
#     dct[i] = dct.get(i,p)
#     p += 1
# if dct[0] >= n or dct[1] >= n:
#     print(dct)
# else:
#
n = int(input())
fib = {}
for i in range(0,n+1):
    fib[i] = fib.get(i,i)
    if i >= 2:
        fib[i] = fib[i-1] + fib[i-2]
    print(fib.values())

