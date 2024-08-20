#Fizz Buzz

#Write a program that prints numbers from 1 to 100. # Loop For
#However, for multiples of 3, print "Fizz" instead of the number, and
#for multiples of 5, print "Buzz."
#for numbers that are multiples of both 3 and 5, print "FizzBuzz."

for num in range(1,101):
    if num%3==0:
        print(f"Fizz {num}")
    elif num%5==0:
        print(f"Buzz {num}")
    if num%5==0 and num%3==0:
        print(f"FizzBuzz {num}")




