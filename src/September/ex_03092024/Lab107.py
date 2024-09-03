class Person:
    #class variables
    #Intsnace variables

    def __init__(self,name):
        self.name=name

    def walk(self, name):
        self.name = name
        print(self.name)
amit =Person('amit')
pramod =Person("suraj")
print(amit.name)
print(pramod.name)

