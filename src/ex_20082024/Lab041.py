# Grade Calculator
#write a program that calculates and displays the letter grade for a given numerical score (e.g A,B,C,F, or F) based on the following grading scale

#A:90-100
#B:80-89
#C:70-79
#D:60-69
#F:0-59

marks=int(input("Enter the marks obtained\n"))

if 90 <= marks <= 100:
    print("A Grade")
elif marks >=80 and marks <=89:
    print("B Grade")
elif marks >=70 and marks <=79:
    print("C Grade")
elif marks >=60 and marks <=69:
    print("D Grade")
elif marks >100 and marks<=0:
    print("You are a super man")
else:
    print("F Grade")
