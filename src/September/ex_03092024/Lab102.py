class Calc:
    def __init__(self):
        print("DC")

    def sum(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return (a /b)

obj=Calc()
a= int(input("Enter the value of a"))
b=int(input("Enter the value of b"))

sub_obj=obj.sub(a,b)
div_obj=obj.div(a,b)
sum_obj=obj.sum(a,b)
mul_obj=obj.mul(a,b)

print(sub_obj,div_obj,mul_obj,sum_obj)