s = 'lOgina360'
v_count = 0
for i in range(len(s)):
    if s[i].lower()=='a'or s[i].lower()=='e' or s[i].lower()=='i' or s[i].lower()=='o' or s[i].lower()=='u':
        v_count+=1
print(v_count)
v_count=0
for i in range(len(s)):
    if s[i].lower() in 'aeiou':
        v_count += 1
print(v_count)


