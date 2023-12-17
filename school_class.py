class school:
    school_name = 'ABC school'
    prin = 'kala'   #class attribute, which is common to all object
    def __init__(self,name,age):
        self.name = name    #obj attributes
        self.age = age

    def show(self):
        print(self.name)
        print(self.age)
        print(self.prin)
    def change_name(self,name2): #obj method
        self.name = name2
    @staticmethod
    def show_address():     #staticmethod
        print('Chennai,velachery')
    @classmethod
    def change_prin(cls,new_pric):
         cls.prin = new_pric #school.prin = 'ganesh'


s1 = school('kumar',19)   #constructor ,call __init__ method
print(s1.prin)
school.change_prin('ganesh')
print(s1.prin)


