for i in range(1,100000):
    if i <= 9:
        print(i)
    elif len(str(i)) % 2 == 0:
        j = int(len(str(i))/2)
        k = str(i)[j:]
        if str(i)[:-j] == k[::-1]:
            print(i)
    elif len(str(i)) % 2 != 0:
        j = int(len(str(i)) // 2)
        k = str(i)[(j+1):]
        if str(i)[:j] == k[::-1]:
            print(i)


