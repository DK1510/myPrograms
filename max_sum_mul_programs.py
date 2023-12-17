# sum of values in list
l = [2,3,4,5,6]
sum = 0     #initialize
for i in range(0,5,1):
    sum += l[i]   #sum = sum + l[i]

print(sum)

# multiplication of values in list
l = [2,3,4,5,6]
mul = 1     #initialize
for i in range(0,5,1):
    mul *= l[i]   #mul = mul * l[i]

print(mul)


#To find max in list
l = [2,3,6,5,4,6]
leng = len(l)
max = l[0]  #initialize
for i in range(1,leng,1):
    if l[i]>max:
        max = l[i]
print(max)




# To find min in a list
l = [2,3,6,5,4,6]
leng = len(l)
min = l[0]  #initialize
for i in range(1,leng,1):
    if l[i]<min:
        min = l[i]
print(min)







