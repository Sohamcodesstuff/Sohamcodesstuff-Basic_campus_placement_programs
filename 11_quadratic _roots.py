from math import sqrt


print("according to the equation ax^2 + bx + c")
a = float(input("enter a = "))
b = float(input("enter b = "))
c = float(input("enter c = "))

try:
    root1 = (-b + (sqrt((b**2)-(4*a*c))))/2*a
    root2 = (-b - (sqrt((b**2)-(4*a*c))))/2*a
    print("roots are",root1,"and",root2)
except:
    print("The equation entered has no valid roots")