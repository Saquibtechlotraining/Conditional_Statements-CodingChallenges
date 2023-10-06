# Write a python program to accept the percentage from the user and display the category according
# to the following criteria:
# Percentage             Category
# <40                     Failed
# >=40 and <55            Fair
# >= 55 and <65           Good
# >= 65                   Excellent

percentage = float(input("Enter the percentage:"))
if percentage < 40:
    category = "Failed"
elif percentage >= 40 and percentage < 55:
    category = "Fair"
elif percentage >= 55 and percentage < 65:
    category = "Good"
elif percentage >= 65:
    category = "Excellent"
print(category)