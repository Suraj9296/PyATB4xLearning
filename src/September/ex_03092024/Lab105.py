a=10
class Person:
    b=11

    def print_info(self):
        global a
        a="hello"
        print(a)
        print(self.b)

obj_ref =Person()
obj_ref.print_info()
