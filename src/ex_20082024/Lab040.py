# Problem find the max between 3 numbers

# Logic Building
num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
num3 = int(input("Enter the third number"))

# if elif else

if num1 > num2 and num1 > num3:
    print(f"{num1}  is maximum number")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is maximum")
else:
    print(f"{num3} is maximum")
