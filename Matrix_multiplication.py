m1 = [[2,3,1],
     [1,2,2]]  #2x3  3x3

m2 = [[1,2,3],
     [4,5,6],
     [7,8,9]]  #3x3
mul= []

if len(m1[0])!=len(m2):
     print('mat mul is not possible')
res =0
for i in range(len(m1)):
     mul.append([])
     for j in range(len(m2[0])):
          for k in range(len(m2)):
               res += m1[i][k]*m2[k][j]
          #res = (m1[i][0]*m2[0][j])+(m1[i][1]*m2[1][j])+(m1[i][2]*m2[2][j])
          mul[i].append(res)
          #mul[i][j] = res
     res = 0
print(mul)
'''r = len(m)
print(r)
print(len(m[0]))
'''