n = [11,2,3,41,5,6,7,8,9,10,11, 1000, 1,-2,-1]
# def fun(n):
#     while True:
#         try:
#             for j in n:
#                 if j % 2 != 0:
#                     print(j,222)
#                     yield j
#         except StopIteration:
#             break
# g = fun(n)
# for i in range(len(n)):
#     print(next(g), end =" ")

def fun(n):
    for j,i in enumerate(n):
        if n[j] % 2 != 0:
            # print(j,i)
            yield i
            j += 1
g = fun(n)

for i in range(len(n)):
    while True:
        try:
            print(next(g), end =" ")
        except StopIteration:
            break

