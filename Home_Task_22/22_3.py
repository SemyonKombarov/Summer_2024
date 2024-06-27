lst = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def',
'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

n = "False gbnfgj pasdv or sdlvnnj raise"
lst1 = []
print("Строка на входе ", n)
for i in n.split():
    if i in lst:
        lst1.append("kw")
    else:
        lst1.append(i)

k = " ".join(lst1)
print('Строка на выходе ',k)