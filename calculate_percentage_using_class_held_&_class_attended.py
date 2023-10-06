# A student will not be allowed to sit in exam if his attendance is less than 75 percent.
# Ask how many classes were held and how many classes were attended and calculate his percentage.
# EXAMPLE 1:

# Number of classes held : 100
# Number of classes attended : 50
# Attendance Percentage : 50.0%
# You are not allowed to sit in exam.

# EXAMPLE 2:

# Number of classes held : 100
# Number of classes attended : 75
# Attendance Percentage : 75.0%
# You are  allowed to sit in exam.

classes_held = int(input("Number of classes held:"))
classes_attend = int(input("Number of classes attend:"))

attendence_percentage = (classes_attend * 100) / classes_held

print("Attendence Percentage:", attendence_percentage, "%")

if attendence_percentage >= 75:
    print("You are allowed to sit in the exam")

else:
    print("You are not allowed to sit in the exam")

