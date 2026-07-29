#string operations
#Indexing


name = "Sharanjani"
print(name[0])
print(name[3])
print(name[9])


#Negative Indexing

name = "Sharanjani"
print(name[-1])
print(name[-2])
print(name[-5])

#Slicing

name = "Sharanjani"
print(name[0:4])
print(name[4:8])
print(name[2:7])

#Length of String

name = "Sharanjani"
print(len(name))



#Convert to Uppercase

city = "chennai"
print(city.upper())

#Convert to Lowercase

city = "CHENNAI"
print(city.lower())

#Capitalize First Letter

name = "python"
print(name.capitalize())

#Count Characters
word = "Apple"
print(word.count("a"))


#Find a Character

word = "computer"
print(word.find("p"))

#Check Starting Word
text = "Python Programming"
print(text.startswith("Python"))

#Split a String
text = "Apple,Mango,Grapes"
print(text.split(","))

#Join Strings
fruits = ["Apple", "Mango", "Grapes"]
print(" - ".join(fruits))

#Python String Slicing

name = "Sharanjani"
print(name[0:4])
print(name[2:7])
print(name[5:10])

#Python String Ranging

name = "Sharanjani"
print(name[:5])
print(name[5:])
print(name[:])

#String methods 
#Concatenating


first_name = "Sharan"
last_name = "Jani"
full_name = first_name + " " + last_name
print(full_name)

#Repetition
#Python String Repetition examples using the * operator with explanations.
#Repeat a Word

word = "Hello "
print(word * 3)

#Repeat a Name
name = "Sharanjani "
print(name * 2)

#Print Stars

star = "*"
print(star * 10)

#Repeat a Character
letter = "A"
print(letter * 5)

#Formatting using format()
name = "Sharanjani"
course = "Python"
print("My name is {}.".format(name))
print("I am learning {}.".format(course))

#Formatting using Index
fruit = "Apple"
price = 120
print("Fruit: {0}".format(fruit))
print("Price: ₹{1}".format(fruit, price))

#Python String Supporting Functions (String Dotted Functions)
#upper() – Converts to Uppercase

name = "sharanjani"
print(name.upper())

#lower()
name = "SHARANJANI"
print(name.lower())

#capitalize()
course = "python"
print(course.capitalize())

#title()
text = "python programming"
print(text.title())

#count()
word = "banana"
print(word.count("a"))

#find()
text = "computer"
print(text.find("p"))

#replace()
text = "I like Java"
print(text.replace("Java", "Python"))

#strip()
name = "   Sharanjani   "
print(name.strip())

#split()
text = "Apple,Mango,Grapes"
print(text.split(","))

#startswith()
text = "Python Programming"
print(text.startswith("Python"))

#endswith()
text = "resume.pdf"
print(text.endswith(".pdf"))

#len()
name = "Sharanjani"
print(len(name))

#swapcase()
text = "Python Programming"
print(text.swapcase())

#isupper()
text = "PYTHON"
print(text.isupper())

#islower()
text = "python"
print(text.islower())

#isalpha()
text = "Python"
print(text.isalpha())

#isdigit()
text = "2026"
print(text.isdigit())

#isalnum()
text = "Python123"
print(text.isalnum())

#center()
text = "Python"
print(text.center(15))

#ljust()
text = "Python"
print(text.ljust(12, "-"))

#rjust()
text = "Python"
print(text.rjust(12, "-"))

#zfill()
number = "45"
print(number.zfill(5))

#index()
text = "Programming"
print(text.index("g"))


#join()
letters = ["P", "Y", "T", "H", "O", "N"]
print("-".join(letters))


#casefold()
text = "PYTHON"
print(text.casefold())





