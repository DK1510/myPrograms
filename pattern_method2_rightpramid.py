
if __name__ == '__main__':
    starc = 1
    spacec = 3
    space = ' '*spacec
    star = '*'*starc
    for i in range(4):
        print(star+space)
        starc+=1
        spacec-=1
        space = ' ' * spacec
        star = '*' * starc
