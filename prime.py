n = 10
prime = 1
#if 7%2 ==0 or 7%3==0 or 7%4==0:
for i in range(2,n):
    if n%i==0:
        prime = 0
        break

if prime ==1:
    print('its prime')
else:
    print('not prime')
