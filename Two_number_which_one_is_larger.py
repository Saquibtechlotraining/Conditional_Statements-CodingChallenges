# Given two numbers, determine which one is larger:-

def larger_number(number_1, number_2):
    if number_1 > number_2:
        return number_1
    else:
        return number_2

if __name__=="__main__":
    number_1 = float(input("Enter the first number:"))
    number_2 = float(input('Enter the second number:'))
    print("Largest Number:",larger_number(number_1, number_2))

