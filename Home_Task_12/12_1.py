n = list(map(int,input().split())) # Вариант ввода №1
def fun (x):
    lst_min = [i for i in range(len(x)) if x[i] == min(x)]
    lst_max = [i for i in range(len(x)) if x[i] == max(x)]
    return lst_min,lst_max
print(fun(n))

n = [int(x) for x in input().split()] # Вариант ввода №2
print(fun(n))
