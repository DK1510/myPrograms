#find identical matrix
r = int(input())
c = int(input())
m1 = []
for j in range(r):
    s = [int(i) for i in input().split()]   #horizontal input
    m1.append(s)
print(m1)

identical = 1
v = m1[0][0]
for i in range(r):
    for j in range(c):
        if i==j:
            if m1[i][j]!=v:
                identical=0
                break
        else:
            if m1[i][j]!=0:
                identical=0
                break
if identical == 1:
    print('identical')
else:
    print('not identical')