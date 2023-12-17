d = {'odd':[], 'even':[],'prime':[]}
for n in range(1,101):
    if n%2 == 0:
        d['even'].append(n)
    else:
        d['odd'].append(n)
    prime = 1
    if n==1:
        continue
    for j in range(2,n):
        if n%j==0:
            prime = 0
            break
    if prime == 1:
        d['prime'].append(n)

print(d['prime'])
