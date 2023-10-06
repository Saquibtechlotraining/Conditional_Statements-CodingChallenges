# Write a program to find the largest of three numbers.

first_number = float(input("Enter the first_number:"))
second_number = float(input("Enter the second number:"))
third_number = float(input("Enter the third number:"))

if first_number > second_number and first_number > third_number:
    print(first_number)

elif second_number > first_number and second_number > third_number:
    print(second_number)

else:
    print(third_number)


