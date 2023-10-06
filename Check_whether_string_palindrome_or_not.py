# Write a program to check whether a given string is palindrome or not:-

def Check_palindrome(string_1):
    string_2 = string_1[::-1]

    if string_1 == string_2:
        return ("String is Palindrome")

    else:
        return ("String is not Palindrome")

if __name__=="__main__":
    string_1 = input("Enter the string")
    print(Check_palindrome(string_1))