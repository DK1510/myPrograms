n = int(input('Enter n: '))
start = n-1
end = n-1

for r in range((n*2)-1):
    for c in range((n*2)-1):
        if c>=start and c<=end:
            print('*',end='')
        else:
            print(' ',end='')
    print('')
    if r<n-1:
        start -=1   #start = start-1
        end+=1
    else:
        start +=1
        end -=1