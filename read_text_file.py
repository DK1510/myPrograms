try:
    f = open('D://Logic_360//test10.txt','r')
    string = f.readline()
    while(string):
        print(string)
        string = f.readline()

except FileNotFoundError:
    print('file not exists')


