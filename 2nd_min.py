l = [-2,-4,1,1,2,3,5]
min = l[0]
min2 = None
for i in range(len(l)):
    if l[i]<min:
        min2 = min
        min = l[i]

    elif (min2==None or l[i]<min2) and l[i]!=min:
        min2 = l[i]

print(min)
print(min2)
