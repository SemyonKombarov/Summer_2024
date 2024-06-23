import pandas as pd

dct = {'Год':[2001,2002,2003,2004,2005],"Товар":["A","B","C","D","E"],"ШТ":[10,20,30,40,50],"Цена":[100,50,30,20,5]}
df = pd.DataFrame(dct)
sum = 0
for i in df.index:
    for j in df.columns:
        x = df.loc[i,j]
        if type(x) != str:
            sum += x
            print(x,end = " ")

print()
print("Сумма всех элементов датафрейма равна",sum)