#Take input and create class in python

class Person:
    def __init__(self):
        self.name=input("Enter the name\n")
        self.age=int(input("Enter the age\n"))
        self.phone =int(input("Enter the phone\n"))
        self.occupation =input("Enter your occupations\n")

    def name_of_the_functions(self):
        print(f"Name is {self.name}")
        print(f"Age is {self.age}")
        print(f"Phone is {self.phone}")
        print(f"Your occupation is {self.occupation}")

person1 =Person()

person1.name_of_the_functions()
