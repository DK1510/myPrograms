n = 4
start = 1
space = 3
for i in range(n*2-1):
    print(' * '*start+'   '*space)
    if i<n-1:
        start+=1
        space-=1
    else:
        start-=1
        space+=1
