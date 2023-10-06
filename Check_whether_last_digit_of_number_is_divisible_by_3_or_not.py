# Write a program to check whether the last digit of the number is divisible by 3 or not.
# Take Number from user and your output must contain the number.

number = int(input("Enter the number:"))
if (number % 10 % 3) == 0:
    print("The last digit of the number is divisible by 3:", number)
else:
    print("The last digit of the number is not divisible by 3", number)