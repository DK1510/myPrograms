l = [4,2,25,6,4]
n = len(l)

#Bubble sort
for i in range(n-1):
    for j in range(n-i-1):
        if l[j] > l[j+1]:
            (l[j],l[j+1]) = (l[j+1],l[j])

print(l)
