#Как решить в одну строку?

n = int(input())
lst = [[x] * x for x in range(1,n+1)]
lst = [x for i in lst for x in i]
print(*lst)
