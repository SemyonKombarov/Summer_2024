n = "abccba"
def palindrom(n):
    # print(n)
    lenght = len(n)
    # print(lenght, 1)
    if lenght <= 1:
        print(True)
        return True
    if n[0] != n[-1]:
        print(False)
        return False
    return palindrom(n[1:lenght-1])

palindrom(n)
