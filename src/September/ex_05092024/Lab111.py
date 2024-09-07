class Myclass:
    #public var
    public_var ="I am PUBLIC"

    #private variable
#    __private_var = "I am private" # cannot access this outside the class

    #protected variable
    _protected_var =" I am protected" # available only in same module

object = Myclass()
print(object.public_var)
#print(object.__private_var)
print(object._protected_var)


