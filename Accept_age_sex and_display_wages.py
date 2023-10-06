age = int(input("Enter the age:"))
if (age >= 18 and age < 30):
    gender = input("Enter the gender:").upper()
    if gender == "M":
        wage = 700
        print("Wage:", wage)

    else:
        if gender == "F":
            wage = 750
            print("Wage:", wage)

        else:
            print("Inappropriate gender")

elif (age >= 30 and age <= 40):
    gender = input("Enter the gender:").upper()
    if gender == "M":
        wage = 800
        print("Wage:", wage)

    else:
        if gender == "F":
            wage = 850
            print("Wage:", wage)

        else:
            print("Inappropriate gender")

else:
    print("Inappropriate age:")