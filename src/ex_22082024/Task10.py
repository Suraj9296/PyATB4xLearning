#Factorial n = 5 5! -->54321 -> 120 3! -> 321 -> 6 4! -> 432*1 -> 24

fn= int(input("Enter the number to find factorial"))
fact=1
if fn==0:
    print(" Factorial of 0 is 1")
elif fn<0:
    print(" We cant find factorial for negative number")
else:
    for i in range(1,fn+1):
        fact=fact*i
    print(fact)
