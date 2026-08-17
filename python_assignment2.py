#Write a program to extract values between quotation marks of a string.

import re

text = 'My name is "Sharanjani" and I am learning "Python".'

result = re.findall(r'"(.*?)"', text)

print(result)

#Write a program to convert snake case string to camel case string

s = input("Enter a snake case string: ")

words = s.split("_")

camel_case = words[0] + "".join(word.capitalize() for word in words[1:])

print("Camel case string:", camel_case)


#Here is a simple Python program to check whether a given year is a leap year

year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")


#Write a program to convert a string to datetime

from datetime import datetime

date_string = "17-08-2026"

date = datetime.strptime(date_string, "%d-%m-%Y")

print("Date:", date)


#Write a function that accepts a string and calculate the number of upper case letters and lower case letters.

def count_letters(string):
    upper = 0
    lower = 0

    for char in string:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1

    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)


string = input("Enter a string: ")
count_letters(string)


#Write a function that takes a list and returns a new list with unique elements of the first

def unique_elements(my_list):
    new_list = []

    for item in my_list:
        if item not in new_list:
            new_list.append(item)

    return new_list


my_list = [10, 20, 10, 30, 20, 40, 30]

print("Original list:", my_list)
print("Unique list:", unique_elements(my_list))


#Write a function that takes a number as a parameter and check the number is prime or not.

def check_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


number = int(input("Enter a number: "))

if check_prime(number):
    print("Prime number")
else:
    print("Not a prime number")


#Write a program to print the even numbers from a given list.

numbers = [10, 15, 20, 25, 30, 35, 40]

print("Even numbers:")

for number in numbers:
    if number % 2 == 0:
        print(number)


#Write a function to check whether a number is perfect or not.

def check_perfect(number):
    total = 0

    for i in range(1, number):
        if number % i == 0:
            total += i

    if total == number:
        return True
    else:
        return False


number = int(input("Enter a number: "))

if check_perfect(number):
    print("Perfect number")
else:
    print("Not a perfect number")



#Write a program to reverse a string word by word. 

string = input("Enter a string: ")

words = string.split()

reverse_words = words[::-1]

result = " ".join(reverse_words)

print("Reversed string:", result)
    
