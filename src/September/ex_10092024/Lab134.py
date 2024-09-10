print("start of the program")
try:
    a = int(input("ent the num1"))
    b=int(input("ent the num2"))
    c=a/b
    print("result div is", c)
except Exception as e:
    print(e)
    print("please check your inputs it should not be a string or zero")
print("end of the program")