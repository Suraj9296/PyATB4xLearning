class GF:
     def car(self):
         return "Old car"


class F(GF):
    def car(self):
        return "hONDA"


class S(F):
    def car(self):
        return "Lambo"

son =S()
print(son.car())