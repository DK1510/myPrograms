import random
screte = random.randint(1,100)
print(screte)
chance = 4
user_input = int(input('Enter an number: '))
while user_input!=screte and chance>0:
    if user_input<screte:
        print('the entered number was less than screte')
    elif user_input>screte:
        print('the entered number was greater than screte')

    user_input = int(input('Enter an number: '))
    chance-=1
    print('chance remaining ',chance)

if screte==user_input:
    print('congratulation you won!!!')
else:
    print('chance expired')