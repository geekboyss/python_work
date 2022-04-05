class Employee():
    def __init__(self, first, last, money):
        self.first = first
        self.last = last
        self.money = money

    def give_raise(self, add=5000):
        self.money = self.money + add
