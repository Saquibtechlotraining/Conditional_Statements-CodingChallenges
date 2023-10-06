# create a sign up and login portal where takes the user- ID and password from user and Sign-up and then ask him to login
#  And if the credientials  matches print ("welcome to Python session"), And if the user-Id match and password
#  unmatached print("Invalid Password"), And if the user-Id unmatch and password match print("Invaliud User-id"), And
# if  both user-Id and password unmatch print("Invalid User-Id and Invalid Password").

print("Create User ID")
print("Create Password")

original_user_Id = "saquiblenovo0001@gmail.com"
original_password = "saquib_consoleflare"
original_crediential = "I am a datascientist"

user_id = input("Enter the user ID").lower()
password = input("Enter the password").lower()

if user_id == original_user_Id and password == original_password:
    print("Login Page")
    crediential= input("Enter the crediential")

    if crediential == original_crediential:
        print("Welcome to python session")
    else:
        print("Invalid Crediential")

if user_id !=  original_user_Id and password == original_password:
    print("Invalid User ID")

if user_id == original_user_Id and password != original_password:
    print("Invalid Password")

if user_id != original_user_Id and password != original_password:
    print("Invalid User Id and Invalid Password")