
s = ' 8(913)828-74-77, +7(913)828-74-77 , +7(812)828-74-77,+7(812)828-7477, +7(912)828-74-77, +8(912)828-74-77, +7(912)828-7477'

def f(s):
    import re
    p1 = r'\+7\(812\)\d\d\d\-\d\d-\d\d|\+7\(812\)\d\d\d\-\d\d\d\d|\+7\(912\)\d\d\d\-\d\d\-\d\d|\+7\(912\)\d\d\d\-\d\d\d\d'
    return(print(*re.findall(p1,s)))


f(s)