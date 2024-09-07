class Parent:
    gold ="2KG"

    def BHK2(self):
        print("2BHK")
class Child(Parent):

    def BHK3(self):
        print("3BHK")

parent_obj=Parent()
child_obj=Child()

print(child_obj.gold)
child_obj.BHK3()
child_obj.BHK2()


