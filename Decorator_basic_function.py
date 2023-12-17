
def make_pretty(func):   #outer fun /decorator fun
    def inner():
        print('inner')
        func()
    return inner

@make_pretty
def ordinary():
    print('ordinary')


# dec_fun = make_pretty(ordinary) #inner == dec_fun
# dec_fun()
ordinary()

