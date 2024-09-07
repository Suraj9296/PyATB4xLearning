#MultiLevel Inherentence

class GrandFather:
    gold ="2KG"

    def bhk1(self):
        print("1BHK")
class Father(GrandFather):
    diamond = "22 Karat"

    def bhk2(self):
        print("2bhk")
class Son(Father):
    btc ="1BTC"

    def bhk3(self):
        print("3BHK")

s= Son()
f = Father()
gf =GrandFather()
