# Take three sides (number) from the user and tell whether the triangle is isosceles, scalene and equilateral
# triangle.

a = float(input("Enter the first side:"))
b = float(input("Enter the second side:"))
c = float(input("Enter the third side:"))

if a == b and b == c and c == a:
    print("Equilateral triangle")

if a != b and b != c and c != a:
    print("Scalene traingle")

if a == b and b != c:
    print("Isosceles triangle")

if a != b and c == a:
    print("Isosceles triangle")

if c != a and c == b:
    print("Isosceles triangle")
