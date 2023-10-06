# Apple considers any iPhone with a battery health of % or above, to be in optimal condition.
# Given that your iPhone has %battery health, find whether it is in optimal condition.
# Take Battery Health from User and print YES if in optimal condition and NO if not.

user_iphone_battery = int(input("Enter the user Iphone battery % health:"))

Apple_consider_iphone_battery_heath = 80

if user_iphone_battery >= Apple_consider_iphone_battery_heath:
    print("YES User Iphone battery health is in optimal condition")

else:
    print("NO User Iphone battery health is in optimal condition")

