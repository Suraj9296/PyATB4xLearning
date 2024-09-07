#Hierarchical Inheritence

class Father:

    def BHK3(self):
        print("3 BHK")

class Pramod(Father):
    def BHK2(self):
        print("2BHK")

class Amit(Father):
    def BHK4(self):
        print("4BHK")

class Lucky(Father):
    def No_house(self):
        print("No house")

pramod=Pramod()
pramod.BHK2()
pramod.BHK2()

amit=Amit()
amit.BHK4()
amit.BHK3()


