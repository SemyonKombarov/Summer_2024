def func(*args,**kwargs):
    return 2

def deco(f):
    import inspect
    def wrapper():

        return inspect.getargspec(f)
    return wrapper

import inspect
# @deco
func(1,2,3,"bb",x=123,b="ddd")
print(locals())
