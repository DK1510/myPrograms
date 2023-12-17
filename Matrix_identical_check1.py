mat = [[2,0,0],[0,2,0],[0,0,2]]
a = mat[0][0]
flag =0
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if i==j:
            if a!=mat[i][j]:
                flag = 1
                break
        else:
            if mat[i][j]!=0:
                flag=1
                break
if flag==1:
    print('not identical')
else:
    print('identical')
