# Write a program to display ‘Hello’ if the number entered by user is multiple of 5 otherwise prints ‘Bye’.

number = int(input("Enter the number:"))
if (number % 5) == 0:
    print("Hello")
else:
    print("Bye")