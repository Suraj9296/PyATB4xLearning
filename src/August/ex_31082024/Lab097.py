class person:
    #attributes
    id= None
    name = None
    age= None
    email =None
    height =None
    gender =None
    phone_no =None
    address = None

    #behaviour
    def talk(self): #self will be first argument in every behaviour
        print("I can talk")
    def sleep(self,name):
        print("I am a method!!")
        return None
    def walk_return(self):
        return "I am walking"
#create an object of class
tushar =person()
tushar.name ="Tushar"
print(tushar.name)

suraj =person()
suraj.name ="Suraj"
print(suraj.name)
