from person import Person

class Book():
    def __init__(self,title,first, last, age,edition,ISBN_number,publisher,year_published,quantity,price):
        self.title = title
        self.author = Person(first, last, age)
        self.edition = edition
        self.number = ISBN_number
        self.publisher = publisher
        self.year = year_published
        self.quantity = quantity
        self.price = price

    def textbook(self):
        print(f"{self.title}, {self.author}, {self.edition}, {self.number}, {self.price}, {self.year}, {self.quantity}, {self. price}")

    def add(self,qty):
        self.quantity = self.quantity + qty

    def deduct(self,qty):
        if self.quantity >= qty:
            self.quantity = self.quantity - qty
            return 0
        else:
            return 1

