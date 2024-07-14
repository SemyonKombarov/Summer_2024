n1 = 'CBAABC'
n2 = "DEFFED"
lst1 = []
lst2 = []
lst1_1 = []
lst2_2 = []
for i in n1:
    if i not in lst1:
        lst1.append(i.upper())
for i in n2:
    if i not in lst2:
        lst2.append(i.upper())
for i in n1:
    lst1_1.append(lst1.index(i))
for i in n2:
    lst2_2.append(lst2.index(i))
print(f"""Слова "{n1}" и "{n2}" изоморфные? {lst1_1 == lst2_2}""")