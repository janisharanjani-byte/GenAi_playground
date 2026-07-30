#Primitive Data Types
#Set (set)

#set is an unordered collection of data items.
#set values are unindexed
#set never supports duplicate
#set supports heterogenous value


#Create a Set

fruits = {"Apple", "Banana", "Orange"}
print(fruits)
print(type(fruits))


#Duplicate Values

numbers = {10, 20, 30, 20, 10}
print(numbers)


#Add an Element

colors = {"Red", "Green", "Blue"}
colors.add("Yellow")
print(colors)

#Remove an Element

animals = {"Dog", "Cat", "Rabbit"}
animals.remove("Cat")
print(animals)

#Check an Element

fruits = {"Apple", "Banana", "Orange"}
print("Apple" in fruits)
print("Mango" in fruits)


#Length of a Set

cities = {"Chennai", "Madurai", "Salem", "Trichy"}
print(len(cities))

#Iterate Through a Set

colors = {"Red", "Green", "Blue"}
for color in colors:
    print(color)


#Clear a Set
    
numbers = {1, 2, 3, 4}
numbers.clear()
print(numbers)

#Student Roll Numbers

roll_numbers = {101, 102, 103, 104}
print(roll_numbers)

#Remove Duplicate Values

marks = {90, 85, 90, 75, 85}
print(marks)


#Add Multiple Elements

numbers = {10, 20, 30}
numbers.update([40, 50])
print(numbers)

#Union of Two Sets

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))


#Intersection of Two Sets

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.intersection(set2))


#Difference of Sets

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
print(set1.difference(set2))


#Empty Set

empty_set = set()
print(empty_set)
print(type(empty_set))


#Non primitive datatypes
##Primitive Data Types
#Dictionary (dict)

#Dictionary is not indexed
#Dictionary ordered collection of data items
#Duplicate values are not followed
#Insted of indexing dictionary follows {Key:value} as a paired items.


#len()

bike = {
    "Brand": "Yamaha",
    "Model": "R15",
    "Color": "Blue",
    "Price": 185000
}
print(len(bike))

#keys()

bike = {
    "Brand": "Honda",
    "Model": "Shine",
    "Color": "Red"
}
print(bike.keys())


#values()

bike = {
    "Brand": "Honda",
    "Model": "Shine",
    "Color": "Red"
}
print(bike.values())


#items()
bike = {
    "Brand": "TVS",
    "Model": "Apache",
    "Price": 150000
}
print(bike.items())

#get()

bike = {
    "Brand": "Royal Enfield",
    "Model": "Classic 350"
}
print(bike.get("Brand"))

#update()

bike = {
    "Brand": "Bajaj",
    "Model": "Pulsar"
}
bike.update({"Color": "Black"})
print(bike)


#pop()

bike = {
    "Brand": "KTM",
    "Model": "Duke",
    "Color": "Orange"
}
bike.pop("Color")
print(bike)


#popitem()

bike = {
    "Brand": "Hero",
    "Model": "Splendor",
    "Color": "Black"
}
bike.popitem()
print(bike)


#clear()

bike = {
    "Brand": "Suzuki",
    "Model": "Gixxer"
}
bike.clear()
print(bike)


#copy()

bike = {
    "Brand": "Yamaha",
    "Model": "FZ"
}
new_bike = bike.copy()
print(new_bike)


#Decision making stataments
#conditional stataments

#if
#if the given test condition is satified then it prints something
#if not satisfied it prints nothing

#conditional statements:-
#-----------------------
#if :-
age = 20

if age >= 18:
    print("Eligible to vote")

#if a single value to be checked with multiple test conditions
#if else:-
age = 16

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

#elif:-
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")












