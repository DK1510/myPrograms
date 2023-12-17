if __name__ == '__main__':  #program starts in main
    s = input('Enter brackets: ')
    b = 0
    for bracket in s:
        if bracket == '(':
            b+=1
        else:
            b-=1
        if b<0:
            break
    if b==0:
        print('equal..')
    else:
        print('Not equal')


