#Encapsulation

class Car:
    name =None
    model=None
    password =123

    def __init__(self):
        print("DC")

    def change_pwd(self):
        self.password ="suraj"

car_obj=Car()
print(car_obj.password)
car_obj.change_pwd()