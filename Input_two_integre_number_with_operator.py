# Design a Program to input two integers num1, num2 and a character(opr).
# The Variable opr reads only one of the four characters(+,-,/,*). Your Program should perform the operation on the
# basis of operator on num1, num2. In case of subtraction, subtract smaller number from bigger number and in case of
# division divide the greater number by smaller numbers.

# Print Integers and result

print("----Calculation----")
print("Addition")
print("Subtraction")
print("Multiplication")
print("Division")

num_1 = int(input("Enter the first number:"))
num_2 = int(input("Enter the second number:"))
operator = input("Enter the operator (+, -, *, /):")

if operator == "+":
    print("Addition of:", num_1, "+",  num_2, "=", num_1 + num_2)

elif operator == "-":
    if num_1 > num_2:
        print("Subtraction of:", num_1, "-", num_2, "=", num_1 - num_2)
    else:
        print("Subtraction of:", num_2, "-", num_1, "=", num_2 - num_1)

elif operator == "*":
    print("Multiplication of:", num_1, "*", num_2, "=", num_1 * num_2)

elif operator == "/":
    if num_1 > num_2:
        if num_2 == 0:
            print("Denominator cannot be zero")
        else:
            print("Division of:", num_1, "/", num_2, "=", num_1 / num_2)

    else:
        if num_1 == 0:
            print("Denominator cannot be zero")

        else:
            print("Division of:", num_2, "/", num_1, "=", num_2 / num_1)
else:
    print("Invalid Input")




