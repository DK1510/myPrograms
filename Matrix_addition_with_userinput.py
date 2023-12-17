
m3 = []
r = int(input())
c = int(input())
m1 = []
for i in range(r):
    l =[int(i) for i in input().split()]
    print(l)
    m1.append(l)
    print(m1)
m2 = []
for i in range(r):
    l =[int(i) for i in input().split()] #get horizontal input in integer in list
    print(l)
    m2.append(l)
    print(m2)

for i in range(r):
    m3.append([])
    for j in range(c):
        print(m3)
        m3[i].append(m1[i][j]+m2[i][j])    #m3[0][0] = m1[0][0]+m2[0][0]
print(m3)
