n = int(input('Enter n:'))
s,e,half = 0,n-1,(n//2)

for i in range(n):
    for j in range(n):
        if i<(half):
            if (s<=j<=e and i%2==0) or (j<s and j%2==0) or (j>e and j%2!=0):
                print('* ',end=' ')
            else:
                print('  ',end=' ')
        else:
            if (s<=j<=e and i%2!=0) or (j<=s and j%2==0) or (j>=e and j%2!=0):
                print('* ',end=' ')
            else:
                print('  ',end=' ')

    if i<half:
        s+=1
        e-=1

    if i>(half)-1 or i==(half)-1:
        s-=1
        e+=1
    print()

