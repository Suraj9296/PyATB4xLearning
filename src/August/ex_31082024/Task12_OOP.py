#Class and Object Assignment


#Create a Employee Class
#A - name,age, phone, address, eid
#B - walk, talk, printdetails,
#with the Constructor which will set the values
#Ask the user about the information for E1, E2
#print the details of the E1, E2 via the print employee functions.


class Employee:
    name=None
    age=None
    phone=None
    address=None
    empId=None

    def __init__(self,name,age,phone,address,empId):
        self.name=name
        self.age=age
        self.phone=phone
        self.address=address
        self.empId=empId

    def walk(self):
        print("Can Walk")
    def talk(self):
        print("Can Talk")
    def printDetails(self):
        print("Name Of Employee is", self.name)
        print("Age of Employee is", self.age)
        print("Phone number of Employee is",self.phone)
        print("Address of Employee is", self.address)
        print("Employee ID of Employee is",self.empId)

name = input("Enter the name of the employee\n")
age=int(input("Enter the age of the Employee\n"))
phone=int(input("Enter the Phone Number of the Employee\n"))
address=input("Enter the Address of the Employee\n")
empId=int(input("Enter the Employee ID  of the Employee\n"))

empDetails = Employee(name,age,phone,address,empId)
empDetails.talk()
empDetails.walk()
empDetails.printDetails()







