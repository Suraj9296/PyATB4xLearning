#Understanding decorators in python

def my_decorator(func):
    #two parts
    #wrapper & call
    def  wrapper():
        print("something is happening before the functions is called")
        func()
        print("something is happening after the functions is called")
    return wrapper()

#defination
@my_decorator
def drive_bike():
    print("I am driving")

#call to the functions

@my_decorator
def drive_scootu():
    print("I am driving sccoty")