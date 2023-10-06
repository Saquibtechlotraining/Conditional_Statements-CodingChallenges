# Write a program to remove all the duplicates character from a given string:-

string = input("Enter the word")
listing_1 = list(string)
print(listing_1)

result = []
for char in listing_1:
    if char not in result:
        result.append(char)
print("".join(result))