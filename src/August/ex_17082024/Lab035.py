# Write a python program to calcualate the area of a circle its radius using the formula

#''' area*pi*r^2''' (Take pie as 3.14)

#Step 1 Figure out the inputs and outputs
#input -->r-->data type -->float
#pi-->3.14
#power-->pow or **-->any

#o/p -->float-area, print area

#step 2

#rough logic == area = 3.14*pow(r,2)

#step3 -- write logic
import math
radius = float(input("Enter the radius of the circle\n"))
print(radius)
area =math.pi*math.pow(radius,2)
print("Area of the circle is", area)
print(f"Area of the circle is {area:.2f}")

#*-->multiply
#**-->power


