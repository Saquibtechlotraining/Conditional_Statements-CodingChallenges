# Write a program to find all the character whose frequency is 1 in a string:-

string = "abcabcdef"
dict = {}
list = []
for char in string:
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1

for char, frequency in dict.items():
    if frequency == 1:
        list.append(char)
print(list)
