from abc import ABC, abstractclassmethod, abstractmethod


class Father(ABC):
    def __init__(self,name):
        self.name =name

    @abstractmethod
    def loan(self):
        pass

class Son(Father):

    def loan(self):
        print("loan clear")

son1=Son("1L")
son1.loan()