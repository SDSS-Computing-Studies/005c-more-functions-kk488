#!python3
"""
Create a function that finds the missing side in a right triangle.
3 input parameters:
float: one side
float: another side
boolean: indicates whether one of the sides is the hypotenuse

return: float length of the missing side

Sample assertions:
assert hypotenuse(12,5,False) == 13
assert hypotenuse(5,3,True) == 4
(2 points)
"""
import math
def hypotenuse(a,b,flag):
    if flag==True:
        if a>b:
            c=float(math.sqrt(a**2-b**2))
        elif a<b:
            c=float(math.sqrt(b**2-a**2))
        return c
    elif flag==False:
        c-float(math.sqrt(a**2+b**2))
        return c
        