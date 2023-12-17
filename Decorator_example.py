def make_pretty(func):  #dec func, func = ordinary_func
    def inner(a,b):
        if b==0:
            return "its can't be divided"
        if a < b:
            a, b = b, a

        return func(a,b)
    return inner
@make_pretty
def div(a,b):
    return a/b
#df = make_pretty(ordinary_fun)  #df = inner
#df()
print(div(2,0))
