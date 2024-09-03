#user defined
#1. They cant return anythins
#2 They can return something
#They have parameters
#They dont have parameters / arguments

#1.NRNP

def greet():
    print("hello")
result = greet()
print(result)

#2 NRWA

def greet_by_name(name):
    print("hello", name)

#3 NRDA

def say_hello_default_arg(name ="pramod"):
    print("hello" , name)
say_hello_default_arg("Suraj")
say_hello_default_arg()
say_hello_default_arg(name ="Chiraksh") # positional argument


def multiple_args(name1="suraj",name2="smruthi",name3="chiraksh"):
    print("Multiple arguments" , name1 , name2,name3)

multiple_args()

#arguments + return type

def sum_of_two_number(num1=22,num2=20):
    return num1+num2
result = sum_of_two_number(10,34)
result = sum_of_two_number(num1=10,num2=34)
print(result)











