#Multiple Inheritance

class Father:

    def father_money(self):

        return 5

    def home(self):

        return "This is from the Father"
class Mother:

    def mother_money(self):

        return 2

    def home(self):

        return "This is from the Mother"

class Son(Mother , Father):  #MRO Method Resolution Order
    pass

s= Son()
print(s.father_money())
print(s.mother_money())
print(s.home())