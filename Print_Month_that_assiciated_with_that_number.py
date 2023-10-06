# Write a program to take number input between 1 and 12 and print the month associated with it.

number = int(input("Enter the number that associated to that month:"))
if number >=1 and number <= 12:
    if number == 1:
        print("January")
    if number == 2:
        print("February")
    elif number == 3:
        print("March")
    elif number == 4:
        print("April")
    elif number == 5:
        print("May")
    elif number == 6:
        print("June")
    elif number == 7:
        print("July")
    elif number == 8:
        print("August")
    elif number == 9:
        print("September")
    elif number == 10:
        print("October")
    elif number == 11:
        print("November")
    elif number == 12:
        print("December")
else:
    print("Invalid Number that associated with no other Month")
