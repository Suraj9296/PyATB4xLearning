#Leap Year Checker
#Create a program that determines whether a given year is a leap year.
#A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
#Use an if-else statement to make this determination.

year=int(input("Enter the Year to be checked\n"))
if year%4==0:
    print("LEAP YEAR")
elif year%100==0 and year%100!=0:
    print("LEAP YEAR")
elif year%400==0:
    print("LEAP YEAR")
else:
    print("NOT A LEAP YEAR")
