class publication:
    company = 'ABC company'
    CM = 'kumar'
    def __init__(self,title,price):
        self.title = title
        self.__price = price + (price / 100) * 5
    def price_incre(self):
        in_price = self.price
        self.price = in_price+(in_price/100)*5

class peroidic(publication):
    def __init__(self, title, publisher, price, period):
        super().__init__(title,price)
        self.__publisher = publisher
        self.period = period

class Book(publication):
    def __init__(self,title,author,pages,price):
        super().__init__(title,price)
        self.author = author
        self.pages = pages

class Magazine(peroidic):
    def __init__(self, title, publisher, price, period):
        peroidic.__init__(self, title, publisher, price, period)


class Newspaper(peroidic):
    def __init__(self, title, publisher, price, period):
        peroidic.__init__(self, title, publisher, price, period)



b1 = Book("wings of fire", "Aldous Huxley", 311, 29.0)
n1 = Newspaper("Ind Times", "India Times Company", 6.0, "Daily")    #construtor
m1 = Magazine("Scientific", "Nature", 5.99, "Monthly")

publication.CM = 'kala'
print(m1.CM)
