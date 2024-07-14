n = [1,1,1,1,1,12]

def iskluchenie(n):
    dct = {i: n.count(i) for i in n}
    minimum = float('inf')
    iskl = 0
    for k,v in enumerate(dct):
        if len(dct) == 1:
            return print(f"Исключений в списке {n} - нет")
        elif dct[v] < minimum:
            minimum = dct[v]
            iskl = v
    return print(f'В списке {n} исключением является число {iskl} c индексом "{n.index(v)}"')

iskluchenie(n)