class Calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def sum(self):
        return self.a + self.b
    def sub(self):
        return self.a-self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return (self.a /self.b)

obj=Calc(3,4)
op1=obj.sum()
print(op1)
