# In a classic chase, Tom is running after Jerry as Jerry has eaten Tom's favourite food.
# Jerry is running at a speed of  metres per second while Tom is chasing him at a speed of  metres per second.
# Determine whether Tom will be able to catch Jerry.
# Note that initially Jerry is not at the same position as Tom.
#
# Take X of Jerry and Y of Tom from the user and make decision and
# print YES if tom can catch and NO if not.

jerry_speed = int(input("Enter the jerry x speed:"))
tom_speed = int(input("Enter the tom y speed:"))

if tom_speed > jerry_speed:
    print("Whether tom will be able to catch jerry:", "YES")
else:
    print("Whether tom will be able to catch jerry:", "NO")