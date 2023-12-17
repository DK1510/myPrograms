n = int(input('enter n:'))
start = n-1
for i in range(n*2-1):
    for j in range(n):
        if j>=start:
            print(' * ',end='')
        else:
            print('   ',end='')
    if i<n-1:
        start-=1
    else:
        start+=1
    print()
