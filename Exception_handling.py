try:    #try this code if error occurs except block will exe
    a =int(input('Enter a :'))
    b = int(input('Enter b:'))
    print(a/b)
    print(a/b)
except (NameError,ZeroDivisionError):
    print("can't div by zero..")
except ValueError:
    print('Please enter only integers')
except Exception as e:
    print(e)
    print('some error occured')
else:
    print('else block exe.....')    # exe only if no error
finally:
    print('finally block')      # always will exe regardless of errors
