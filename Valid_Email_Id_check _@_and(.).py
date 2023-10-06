#Write a program to check whether a given string is a valid email address
# (i.e., it contains exactly one "@" symbol and at least one "." after the "@"):-

string = "saquiblenovo@.gmail.com"
if ("@" in string):
    str = string.split("@")
    if str[1].startswith("."):
        print("Valid email id")
    else:
        print("Invalid email id because . not just present after @")
else:
    print("Invalid email id because @ not present")
