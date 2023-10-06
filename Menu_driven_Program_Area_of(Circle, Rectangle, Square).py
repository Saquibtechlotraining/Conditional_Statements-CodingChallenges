#Write a menu driven program for three options. (Take input of option from user).
# i)              Area of circle
# ii)            Area of Rectangle
# iii)          Area of Square
#Print the area along with sides.

while True:
    print("....Area Calculator....")
    x = '''    1. Area of Circle
    2. Area of Rectangle
    3. Area of Square
    4. Exit    '''
    print(x)

    ch = int(input("Choose Operation:"))
    if ch == 1:
        radius = float(input("Enter the radius of a circle:"))
        pi = 3.14
        print("Area of a Circle:", pi * (radius * radius))

    if ch == 2:
        length = float(input("Enter the length of the rectangle:"))
        breadth = float(input("Enter the breadth of a rectangle:"))
        print("Area of a Rectangle:", length * breadth)

    if ch == 3:
        sides = int(input("Enter the sides of a Square:"))
        print("Area of a Square:", sides * sides)

    if ch == 4:
        break

