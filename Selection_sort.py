#selection sorting
l = [12, 14, 10, 9, 100]
n = len(l)
for i in range(n):
    print(l)
    min_p = i
    for j in range(i+1,n):
        if l[j]< l[min_p]:
            min_p = j

    (l[i], l[min_p]) = (l[min_p],l[i])


print(l)
