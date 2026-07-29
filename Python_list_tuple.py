#Python Native datatypes 
#python collections
#python NON PRIMITVE DATATYPES


#Primitive Data Types
#String (str)

name = "Sharanjani"
print(name)
print(type(name))

#Integer (int)

age = 22
print(age)
print(type(age))

#Float (float)

height = 5.4
print(height)
print(type(height))

#Complex (complex)

number = 4 + 7j
print(number)
print(type(number))


#Boolean (bool)

is_student = True
print(is_student)
print(type(is_student))


#Non-Primitive Data Types (Python Collections)

#List (list)

fruits = ["Apple", "Banana", "Orange"]
print(fruits)
print(type(fruits))

#Tuple (tuple)

colors = ("Red", "Green", "Blue")
print(colors)
print(type(colors))

#Set (set)

numbers = {10, 20, 30, 40}
print(numbers)
print(type(numbers))

#Dictionary (dict)

student = {
    "Name": "Sharanjani",
    "Age": 22,
    "City": "Chennai"
}

print(student)
print(type(student))


#Non primitive datatypes:
#list/tuple
#Enclosed with []
#list contains ordered collection of data items.
#list value are indexed
#list supports duplicate values
#list contains hetrogenous values.


#List of Student Names

students = ["Sharanjani", "Priya", "Rahul", "Arun"]
print(students)
print(type(students))

#Changing a List Item

students = ["Sharanjani", "Priya", "Rahul"]
students[1] = "Anjali"
print(students)

#Adding an Item to a List

students = ["Sharanjani", "Priya", "Rahul"]
students.append("Kiran")
print(students)

#Modifying a List

numbers = [10, 20, 30]
numbers.append(40)
print(numbers)

#Marks List

marks = [85, 90, 78, 95]
print(marks)

#Mixed Data Types

details = ["Rahul", 22, 5.8, True]
print(details)

#Access List Elements

fruits = ["Apple", "Banana", "Orange", "Mango"]
print(fruits[0])
print(fruits[2])


#Change a List Item

colors = ["Red", "Blue", "Green"]
colors[1] = "Yellow"
print(colors)

#Add an Item

numbers = [10, 20, 30]
numbers.append(40)
print(numbers)

#Remove an Item

cities = ["Chennai", "Madurai", "Coimbatore"]
cities.remove("Madurai")
print(cities)


#Find List Length

animals = ["Dog", "Cat", "Rabbit", "Cow"]
print(len(animals))

#Tuple

fruits = ("Apple", "Banana", "Orange")
print(fruits)

#Roll Numbers

roll_numbers = (101, 102, 103, 104)
print(roll_numbers)


#Mixed Tuple

student = ("Priya", 21, True, 85.5)
print(student)

#Access Tuple Elements

colors = ("Red", "Green", "Blue")
print(colors[0])
print(colors[2])


#Find Tuple Length

days = ("Monday", "Tuesday", "Wednesday", "Thursday")
print(len(days))


#Count an Element

numbers = (10, 20, 10, 30, 10)
print(numbers.count(10))


#Find the Index

animals = ("Dog", "Cat", "Rabbit", "Cow")
print(animals.index("Rabbit"))

#Tuple with Different Data Types

employee = ("Ravi", 25, "Developer", 45000)
print(employee)

#Student Names

students = ("Arun", "Priya", "Kavin", "Meena")
print(students)

#Negative Indexing

colors = ("Red", "Green", "Blue", "Yellow")
print(colors[-1])
print(colors[-2])


#Tuple Slicing

numbers = (10, 20, 30, 40, 50)
print(numbers[1:4])

#Find Length of Tuple

animals = ("Dog", "Cat", "Rabbit", "Cow")
print(len(animals))

#Count an Item

marks = (90, 85, 90, 70, 90)
print(marks.count(90))


#Find Index of an Item

cities = ("Chennai", "Madurai", "Salem", "Trichy")
print(cities.index("Salem"))

#Tuple Concatenation

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple1 + tuple2
print(result)

#Tuple Repetition

letters = ("A", "B")
print(letters * 3)

#Check if an Item Exists

fruits = ("Apple", "Banana", "Orange")
print("Banana" in fruits)
print("Mango" in fruits)

#Iterate Through a Tuple

colors = ("Red", "Green", "Blue")
for color in colors:
    print(color)

#Mixed Data Types

employee = ("Rahul", 25, 55000.50, True)
print(employee)

#Single Element Tuple

number = (100,)
print(number)
print(type(number))

#Nested Tuple

student = ("Anu", (85, 90, 95))
print(student)
print(student[1])


#Maximum and Minimum Values

numbers = (12, 45, 8, 67, 23)
print(max(numbers))
print(min(numbers))

#Sum of Tuple Elements

numbers = (10, 20, 30, 40)
print(sum(numbers))


#Convert Tuple to List

fruits = ("Apple", "Banana", "Orange")
fruit_list = list(fruits)
print(fruit_list)

#Unpacking a Tuple

student = ("Sharanjani", 22, "IT")
name, age, department = student
print(name)
print(age)
print(department)


