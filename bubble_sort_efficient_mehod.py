l = [1,2,3,5,4]
n = len(l) #5
for i in range(n):
    swap = 0
    for j in range(n-i-1):
        print(l)
        if l[j]<l[j+1]:
            (l[j],l[j+1]) = (l[j+1],l[j])
            swap = 1
    if swap == 0:
        break
    print()
print(l)
