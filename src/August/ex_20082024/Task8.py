#Write a program that classifies a triangle based on its side lengths. Given three input values representing the lengths of the sides,
#determine if the triangle is equilateral (all sides are equal),
#isosceles (exactly two sides are equal), or scalene (no sides are equal).
#Use an if-else statement to classify the triangle.

L1=float(input("Enter the Length of First Side of Triangle\n"))
L2=float(input("Enter the Length of Second Side of Triangle\n"))
L3=float(input("Enter the Length of Third Side of Triangle\n"))

if L1==L2==L3:
    print("Equilateral Triangle")
elif L1==L2 or L1==L3 or L2==L1 or L2==L3:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")

