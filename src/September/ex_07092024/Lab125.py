#OOPs
#Class -Blueprint
#Object -Instance of class
#Enacapsulation -- private , protected, public
#Inheritance - single, multiple,multilevel, heri,hybrid
#Poly--method overriding, method overlaoding(x)
#self,super,__init__

#Abstraction
#Hide the details and show what is required
#hiding classes (class level)

#car - with key __private, tyres--public

#car --> multiple -- Engine, GearBox
#car --> drivers-->engine, gearbox?

from abc import ABC, abstractclassmethod, abstractmethod


class Animal(ABC):
    def __init__(self,name):
        self.name =name

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
        def sound(self):
            print("Bark")

dog=Dog("PP")
dog.sound()


