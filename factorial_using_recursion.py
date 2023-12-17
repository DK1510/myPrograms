def factorial(n):
    if n<=1:        #Base condition
        return n
    else:           #recursive condition
        return n * factorial(n-1)


print(factorial(5))