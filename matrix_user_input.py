r = int(input('Enter no of r: '))
c = int(input('Enter no of c: '))
mat = []
for i in range(r):
    l = [int(i) for i in input().split()]
    mat.append(l)
print(mat)