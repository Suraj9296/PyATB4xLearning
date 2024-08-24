#Fibonaci series 0, 0 + 1, 0 + 1 + 1, n = 7  0, 1, 2, 3, 5, 8, 13

num=int(input("Enter the number to find Fibonicci Series"))

fib=0
num1=0
num2=1
for i in range(num):
    print(num1)
    fib=num1+num2
    num1=num2
    num2=fib



