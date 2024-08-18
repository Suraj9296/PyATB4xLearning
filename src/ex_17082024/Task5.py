#- Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.

n1=int(input('Enter the first number'))
n2=int(input('Enter the second number'))

if n1==n2:
    print("n1 is equal to n2")
elif n1>n2:
    print("n1 greater than n2")
else:
    print("n1 lesser than n2")

