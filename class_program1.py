class student:
    school = 'ABC school'   #class varibale/attribute
    prin = 'kala'
    def __init__(self,name,age):
        self.name = name    #instance varibale/attributes
        self.age  = age

    def __str__(self):
        return 'its an obj od student class'

    def show(self):     # methods
        print(self.name)
        print(self.age)
        print(self.school)
        print(self.prin)

    def change_age(self,age2):
        self.age = age2

    def show2():
        print('not self...')
        print(student.school)


s1 = student('kumar',12)  #constructor
s2 = student('ganesh',13)

print(s)