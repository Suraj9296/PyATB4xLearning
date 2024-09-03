#- Write a Python program to calculate the area of a circle given its radius using the formula ``` area=π×r^2``` ( Take pie as 3.14)

radius= float(input("Enter the radius of the circle"))
pi=3.14
area_of_circle =pi*radius**2
print(f"area_of_circle is {area_of_circle:.2f}")
