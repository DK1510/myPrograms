#Matrix multiplication
m1 = [[1,2,3],[4,5,6],[7,8,9]]
m2 = [[2,3],[1,5],[1,2]]
m3 = [[0,0],[0,0],[0,0]]
for i in range(len(m1)):
    for j in range(len(m2[0])):
        for k in range(len(m2)):
        #m3[i][j] = m1[i][0]*m2[0][j] + m1[i][1]*m2[1][j] + m1[i][2]*m2[2][j]
            m3[i][j] += m1[i][k]*m2[k][j]
print(m3)