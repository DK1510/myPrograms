l = ['glass','brass','class','cat']
aplha = [chr(i) for i in range(97,123)]
print(aplha)
c = []
count=0
l_leng = len(l)
for letter in aplha:
    for word in l:
        if letter in word:
            count+=1
    if count==l_leng:
        c.append(letter)
    count = 0

print(c)

