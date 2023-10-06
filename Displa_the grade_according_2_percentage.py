# 6: Write a program to accept percentage from the user and display the grade according to the following criteria:-

percentage = float(input("Enter the percentage:"))
if percentage >= 90:
    print("Grade: A")

elif percentage >=80 and percentage <= 90:
    print("Grade: B")

elif percentage >= 60 and percentage < 80:
    print("Grade: C")

else:
    print("Grade: D")