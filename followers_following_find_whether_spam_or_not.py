# Chef categorises an instagram account as spam, if, the following count of the account is more than 10 times the count of followers.
# Given the following and follower count of an account as  and  respectively, find whether it is a spam account.
#
# Take X and Y from the user:-

x = int(input("Enter the count of following:"))
y = int(input("Enter the count of followers:"))

if x > 10 * y:
    print("Yes spam account")
else:
    print("No spam account")