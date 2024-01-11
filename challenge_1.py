#ask the user to enter the lenght of all three sides of a triangle:

import math #this was a quick fix because the program was not recognising "math.squrt" and that was the solution (I quite didn't understand)

side1 = float(input("\nEnter the value referring to one side of the triangle: "))
side2 = float(input("\nEnter the value referring the second side of the triangle: "))
side3 = float(input("\nEnter the value referring the third side of the triangle: "))

print("\nThe value entered is: {},{},{}".format(side1, side2, side3))

#Calculate the high of the triangle
h = (side1 + side2 + side3) / 2 

#Calculate the area of the triangle
area = float(math.sqrt(h * (h - side1) * (h - side2) * (h - side3))) #Heron's formula

print("\nThe area of the triangle is: {}".format(area))

print("\nThank you!\n")