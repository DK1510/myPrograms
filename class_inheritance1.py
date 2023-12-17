from abc import ABC, abstractmethod
class Employee(ABC):    #Abstract class
    com_name = 'XYZ compnay'    #class attribute
    def __init__(self,name,salary,role):
        self.name = name    #public
        self.__salary = salary     #private #instance/object attribute
        self._role = role   #protected

    @abstractmethod
    def show_company(self):
        pass

class Chennai_branch(Employee):
    def __init__(self,name,salary,role,address):
        super().__init__(name,salary,role)      #super() refers to parent class
        self.address = address

    def show_company(self): #instance method
        print(self.com_name)


class Bangalore_branch(Employee):
    def __init__(self,name,salary,role,address):
        super().__init__(name,salary,role)
        self.address = address
    def show_company(self):
        print(self.com_name)



e2 = Chennai_branch('kumar',20000,'Enginner','ECR')
s3 = Bangalore_branch('kumar',20000,'Enginner','ECR')
print(e2.com_name)
print(s3.com_name)


