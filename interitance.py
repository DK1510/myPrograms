from abc import ABC, abstractmethod
class publication(ABC):
    company = 'ABC company'
    CEO = 'sam'
    def __init__(self,title,price):
        self.title = title
        self._price = price
    @abstractmethod
    def show_price(self):
        pass
class periodic(publication):
    def __init__(self,title, publisher, price, period):
        super().__init__(title, price)
        self.publisher = publisher
        self.period = period

class Book(publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title,price)
        self.author = author
        self.pages = pages
    def show_price(self):
        print(self._price)

class Magazine(periodic):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, publisher, price, period)
    def show_price(self):
        print(self._price)

class Newspaper(periodic):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, publisher, price, period)
    def show_price(self):
        print(self._price)

# b1 = Book("wings of f", "Aldous Huxley", 311, 29.0)
# n1 = Newspaper("NY Times", "New York Times Company", 6.0, "Daily")
# m1 = Magazine("Scientific American", "Springer Nature", 5.99, "Monthly")
#
#
# print(b1.author)
# print(n1.publisher)
# print(b1._price, m1._price, n1._price)
# print(b1.CEO)
# print(n1.CEO)
# print(m1.CEO)
# publication.CEO = 'kumar'
# print(b1.CEO)
# print(n1.CEO)
# print(m1.CEO)

