#nested if
#if one test condition is given inside an other test condition.


#Driving License
age = 20
has_license = True

if age >= 18:
    print("Eligible by Age")

    if has_license:
        print("You can drive")
        

#Student Pass and Grade
marks = 85

if marks >= 35:
    print("Student Passed")

    if marks >= 75:
        print("Grade A")


#ATM Withdrawal

balance = 10000
amount = 3000

if balance >= amount:
    print("Balance Available")

    if amount <= 5000:
        print("Transaction Successful")


#Login System
username = "admin"
password = "1234"

if username == "admin":
    print("Username Correct")

    if password == "1234":
        print("Login Successful")



#Looping Statements
    
#looping same set of actions repeated many times till n-1 times based on given condition
#for loop
#while loop
        
#for loop
#CORM Process = Check Once Runs Many Times
#for loop checks the condition only once and runs the loop many times[n-1]
        
##while Loop
#Checks the every single time and runs the loop till the condition is TRUE

        

for i in range (5):
      print(i)


for i in range (0,5):
      print(i)


for i in range (1,6):
      print(i)


for i in range (0,5,1):
      print(i)

      
for i in range (1,11,1):
      print(i)

for i in range (1,11,1):
    print (i,end = ' ')

#print even numbers b/w 1 to 10
    for  i in range (1,11,2):
        print(i,end = ' ')



#print name that starts with 'p'
#Using a for Loop        
names = ["Priya", "Arun", "Pooja", "Kavin", "Preethi"]

for name in names:
    if name.startswith("P"):
        print(name)

#Using Indexing
names = ["Priya", "Arun", "Pooja", "Kavin", "Preethi"]

for name in names:
    if name[0] == "P":
        print(name)


#print name that start with 'vowels '
#Using if Statement
        
names = ["Arun", "Priya", "Indhu", "Kavin", "Uma", "Elan"]

print("Names starting with vowels:")

for name in names:
    if name[0] in "AEIOUaeiou":
        print(name)


#Using if...else

name = "Kavin"

if name[0] in "AEIOUaeiou":
    print("Name starts with a vowel")
else:
    print("Name starts with a consonant")


#Using User Input

name = input("Enter your name: ")

if name[0] in "AEIOUaeiou":
    print(name, "starts with a vowel")
else:
    print(name, "starts with a consonant")



#Using a for Loop

names = ["Arun", "Priya", "Indhu", "Kavin", "Uma", "Elan"]

print("Names starting with vowels:")

for name in names:
    if name[0] in "AEIOUaeiou":
        print(name)








        
      




        
