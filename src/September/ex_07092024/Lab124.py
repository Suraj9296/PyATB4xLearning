#Method overloading:
#Python does not support method overloading
#in the traditional sense

class MathsUtils(object): #is a A object single inheritance
#method - overloading -- Not Supported!
     def add(self,a,b):
         return a+b
     def add(self,a,b,c): #"if we initialize c to any default value the its supported, C=0"
         return a+b+c
math =MathsUtils()
op1=math.add(1,2)
print(op1)

