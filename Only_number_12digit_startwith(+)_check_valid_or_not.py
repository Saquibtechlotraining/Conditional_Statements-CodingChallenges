# You work in a company and you are given customers number, But many customers filled wrong data, so you need
# to check if the number given by customer is right or not.

# Phone Number should match following Criteria :

# Only numbers , spaces and - are allowed though (so few customers wrote their number with spaces.)
# 12 digits only.
# + is allowed , though only at beginning of the number.

# If it matches all the three criterias , Print it is a valid number else
# Print it is not a valid number with the reason why ?

# Example 1:- number = '+91 - 765 - 181 - 1162'
#             Valid Number

# Example 2:- number = '91 - 7651811162'
#             Valid Number


number = input("Enter the number:")
if number[0].startswith("+"):
    num = number.replace(" ", "").replace("-", "")
    if (num[1:].isdigit()):
        if len(num) == 13:
            print("Valid Number")
        else:
            print("Not valid Digit exceeded")
    else:
        print("Not valid only Numbers")
else:
    num = number.replace(" ", "").replace("-", "")
    if (num.isdigit()):
        if len(num) == 12:
            print("Valid Number")
        else:
            print("Not valid digit exceeded")
    else:
        print("Invalid Only Numbers")