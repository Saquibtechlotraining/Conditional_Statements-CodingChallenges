# Write a program to take number input between 1 to 7 and print the day associated to that number such
# as 1 for Sunday, 2 for Monday, etc.

number = int(input("Enter the number that associated to that day:"))
if number >= 1 and number <= 7:
    if number == 1:
        print("Sunday")
    elif number == 2:
        print("Monday")
    elif number == 3:
        print("Tuesday")
    elif number == 4:
        print("Wednesday")
    elif number == 5:
        print("Thursday")
    elif number == 6:
        print("Friday")
    elif number == 7:
        print("Saturday")
else:
    print("Invalid number that associated with day")