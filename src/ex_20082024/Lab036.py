#conditions and loops

#write a program to take a user age and let him know if he can go to club
#21

#logic building
#1 . user input -- data type --> int
#o/p --> string --> user if he can go  or not

#age > 21 -->print can go
#age < 21 print cant go


age = int(input("Enter your age to enter club"))
if age>=21:
    print(" Can go to club")
else:
    print("Cant go to club")