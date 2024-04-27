n = (input("Ввведите целое число "))
#print(n)
print("Количество цифр в представленном числе равно")
for i in range(0,10):
    x = n.count(str(i))
    print(i,"-",x)