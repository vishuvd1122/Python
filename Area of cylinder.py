# Program to find the surface area of a cylinder
r = float(input("Enter radius of a cylinder:"))     # This will take input of the radius from the user
h = float(input("Enter height of a cylinder:"))     # This will take input of the height from the user
area = (2*3.14*r**2)+(2*3.14*r*h)                   # Variable "area" will store the area of cylinder calculated formula
print("Area of cylinder with radius and height of", r, "units and", h, "units respectively:", area, "sq. units")
