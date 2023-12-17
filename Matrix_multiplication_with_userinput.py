#Matrix multiplication
r1 = int(input('Enter m1 r:'))
c1 = int(input('Enter m1 c:'))
r2 = int(input('Enter m2 r:'))
c2 = int(input('Enter m2 c:'))
if c1==r2:
    m1 = []
    for j in range(r1):
        s = [int(i) for i in input().split()]   #horizontal input
        m1.append(s)
    m2 = []
    for j in range(r2):
        s = [int(i) for i in input().split()]   #horizontal input
        m2.append(s)
    m3 = []

    for i in range(len(m1)):
        m3.append([])
        for j in range(len(m2[0])):
            m3[i].append(0)
            for k in range(len(m2)):
            #m3[i][j] = m1[i][0]*m2[0][j] + m1[i][1]*m2[1][j] + m1[i][2]*m2[2][j]
                m3[i][j] += m1[i][k]*m2[k][j]
    print(m3)
else:
    print('sry invalid row col for matrix multiplication....')