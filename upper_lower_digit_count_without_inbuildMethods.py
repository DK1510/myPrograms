s = input('Enter a string:')
s.lower()
u,l,d,sp = 0,0,0,0
upper = [chr(i) for i in range(97,123)]
lower = [chr(i) for i in range(65,65+26)]
digit = [i for i in range(0,10)]
print(upper)
print(lower)
print(digit)
for char in s:
    if char in upper:
        u+=1
    elif char.islower():
        l+=1
    elif char.isdigit():
        d+=1
    else:
        sp+=1
print('upper=',end ='')
