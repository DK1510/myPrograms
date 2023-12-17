class student:
    school = 'ABC school'
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self): #instance method
        print(self.name)
        print(self.age)

    @classmethod
    def class_show(cls):    #class method
        print(cls.school)

    @staticmethod
    def address():  #static method
        print('chennai')




s1 = student('kumar',15)
#s1.show()
student.class_show()
#student.address()
#s1.address()
