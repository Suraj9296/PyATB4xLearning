#Method Overriding Same name in the parent and child
#child always override the parent functions
#super means call my parent function
class GrandFather:
    x=15
    def home(self):
        print("Old Home")

class Father(GrandFather):
    a=10
    def home(self):
        print("1BHK")
        print(self.a)
        print(super().x)

class Son(Father):
    b=12
    def home(self):
        super().home() # Father behaviour by super()
        print(super().a) #Father attributes by super()
        print("No House")
        print(self.b)

pramod=Son()
pramod.home()
print(pramod.x)
