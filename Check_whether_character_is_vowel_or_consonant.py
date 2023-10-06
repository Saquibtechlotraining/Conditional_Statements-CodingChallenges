# Write a program to check whether a given character is a vowel or a consonant:-

character = input("Enter the character")
import string
alphabet = "".join(list(string.ascii_letters))
#print(alphabet)

consonant = alphabet.replace("a", "").replace("e", "").replace("i","").replace("o","").replace("u","").replace("A", "").replace("E", "").replace("I","").replace("O","").replace("U","")
#print(consonant)

vowels = "AEIOUaeiou"

if character in vowels:
    print("character is vowel")

if character in consonant:
    print("character is consonant")