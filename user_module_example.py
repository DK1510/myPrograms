pi = 3.14
def add(a,b):
    return a+b

def factorial(n):
    ''' it accept one arg n and return n!'''    #docstring
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact