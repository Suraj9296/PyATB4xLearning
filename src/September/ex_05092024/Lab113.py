#Inheritence
#Single Inheritence

class Father:
    key ="2bhk"

    def car(self):
        print("Father car!!, ALTO")

class Son(Father):
    pass


father_obj = Father()
father_obj.car()

son_obj= Son()
son_obj.car()