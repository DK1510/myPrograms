def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
        yield fact
def ofactorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact
#print(ofactorial(10000000000))
g = factorial(10000000000)
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))