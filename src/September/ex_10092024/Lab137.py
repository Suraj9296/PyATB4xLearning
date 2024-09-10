try:
    num1 = int(input("Enter a number1"))
    num2 = int(input("Enter a number2"))
    result = num1/num2
except ValueError as ve:
    print( "Value error")
except ZeroDivisionError as zde:
    print("Zero div error")
else:
    print(f"Result is {result}")
finally:
    print("This code will always execute")