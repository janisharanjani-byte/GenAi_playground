#1.Write a program to remove lowercase substrings from a given string.

string = "SHaRAN  JanI"

result = ""

for ch in string:
    if not ch.islower():
        result = result + ch

print("Original String:", string)
print("After removing lowercase:", result)



#Write a program that reads a given expression and evaluates it. 

expression = input("Enter an expression / Computer science: ")

result = eval(expression)

print("Result:", result)


#Write a program to insert spaces between words starting with capital letters

string = input("Enter a string: ")

result = ""

for ch in string:
    if ch.isupper() and result != "":
        result = result + " "
    result = result + ch
    
print("Result:", result)



#Write a program to remove the parenthesis area in a string.

sstring = input("Enter a string: ")

result = ""
inside = False

for ch in string:
    if ch == "(":
        inside = True
    elif ch == ")":
        inside = False
    elif not inside:
        result = result + ch

print("Result:", result)   



#Write a program to split a string with multiple delimiters.


import re

string = "Apple,Orange;Banana|Mango"

result = re.split("[,;|]", string)

print(result)


#Write a program to find all adverbs and their positions in a given sentence.

import re

sentence = input("Enter a sentence: ")

words = sentence.split()

for i, word in enumerate(words):
    if word.lower().endswith("ly"):
        print("Adverb:", word)
        print("Position:", i)

        
#Write a program to do a case-insensitive string replacement. 

import re

string = input("Enter a string: ")
old = input("Enter the word to replace: ")
new = input("Enter the new word: ")

result = re.sub(old, new, string, flags=re.IGNORECASE)

print("Result:", result)


#Write a program to split a string at uppercase letters.

import re

string = input("Enter a string: ")

result = re.split(r'(?=[A-Z])', string)

print(result)


#Write a program to remove everything except alphanumeric characters from a string


string = input("Enter a string: ")

result = ""

for ch in string:
    if ch.isalnum():
        result = result + ch

print("Result:", result)

#Write a program to remove all white spaces from a string

string = input("Enter a string: ")

result = ""

for ch in string:
    if not ch.isspace():
        result = result + ch

print("Result:", result)









    

