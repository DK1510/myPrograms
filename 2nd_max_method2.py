l = [16,3,10,16,4,10,16,16]
max1 = l[0]
for i in range(len(l)):
    if l[i] < max1:
        max1 = l[i]
print(max1)
max2 = 0
for i in range(len(l)):     #initailize
    if l[i] != max1:
        max2 = l[i]
        break
print(max2)
for i in range(len(l)):
    if l[i] < max2 and l[i]!=max1:
        max2 = l[i]
print(max2)

