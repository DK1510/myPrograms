l = [2,4,6,7,9,11]

for j in range(0,len(l),1):
    prime = 1
    n = l[j]
    for i in range(2, n):
        if n % i == 0:
            prime = 0
            break

    if prime == 1:
        print(n, 'is prime')
    else:
        print(n, 'is not prime')


