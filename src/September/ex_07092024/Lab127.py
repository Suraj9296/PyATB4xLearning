from abc import ABC, abstractclassmethod, abstractmethod


class PyATB(ABC):

    @abstractmethod
    def payFee(self):
        pass
    def enrolled(self):
        print("Enrolled")

class Amit(PyATB):
    def payFee(self):
        print("Enroll Amit")

am=Amit()
am.payFee()