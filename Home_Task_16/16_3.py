def deco_lower(func):
    def wrapper():
        func_result = func()
        result = func_result.lower()
        return result
    return wrapper
@deco_lower
def f():
    g = input()
    return g
print(f())