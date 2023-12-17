l = [2,4,3,14,15,10]
e_count = 0 #initaliztion
o_count = 0

for i in range(0,6):  #iteration
    if l[i]%2==0:
        e_count = e_count+1
    else:
        o_count = o_count+1
print(e_count)
print(o_count)
