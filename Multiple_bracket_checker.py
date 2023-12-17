s = input()
l = list(s)
print(l)
d = {'}':'{',  ')':'(',  ']':'['}
i = 0
equal = 1
while(l):
    if not i<len(l):
        equal = 0
        break
    if l[i] in d.keys():
        if l[i-1] == d[l[i]]:
            l.pop(i-1)
            l.pop(i-1)
            i = i-2
        else:
            equal = 0
            break
    print(l)
    i+=1
if equal==1:
    print('equal')
else:
    print('not equal')