#Constructor
#Special Function in class , __init__()
#It will be automatically called when you create an object

class Dog:

    def __init__(self,name):
        print("I will be automatically called when you create an object")
        self.name=name

    def sleep(self):
        print("Sleeping")

dog1= Dog("mow")
dog1.sleep()

dog2=Dog("chow")
print(dog2.name)