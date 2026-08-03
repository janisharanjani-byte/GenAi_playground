#While loop
#Checks the every single time and runs the loop till the condition is TRUE
#it is mandate to give the incremental /decremental value in while loop.
#otherwise the loop will exective infinite times


#flow control statements:

#break
#continue
#Pass

#break---------->It terminate the execution of a loop when certain condition is met

for i in range (10):
    print (i,end = '')


for i in range(10):
    print(i,end='')
    if i==5:
        break
    
for i in range(0,10,1):
    print(i,end='')


#Continue

for i in range (10):
        print (i,end='')


#Display number between 10 to 20 and skip number 15 and 18
        

for i in range(10, 21):
    if i == 15 or i == 18:
        continue
    print(i)

cities = ['Delhi', 'Chennai', 'Pune', 'Salem', 'Mumbai', 'Goa']
# Display the name whose count is not exactly 5 using FCS

cities = ['Delhi', 'Chennai', 'Pune', 'Salem', 'Mumbai', 'Goa']

for city in cities:
    if len(city) != 5:
        print(city)


#Display the names whose count is exactly 5 using FCS        
    for i in cities:
        if len(i)==5:
            print(i)

#Pattern Programs

for i in range (5):
    print(i,end='')
    

for i in range (5,0,-1):
    print(i,end='')
    
#Right Angle Triangle (RAT)- Using nested for loop
rows = 5

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
    
rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print(i, end=" ")
    print()



# i-represent outer for loop/Row printing/Which number to print
# j-represent outer for loop/Colum printing/How many times to print
#Star Pattern
for i in range(1,6):
    for j in range(0,i):
        print("*", end=" ")
    print()


for i in range(1, 6):
    for j in range(0,i):
        print(chr(i+64), end=' ')
    print()

#INVERSE RAT PATTERN PRINTING
#Row printing
    
#Inverse Star Pattern
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


#colum printing
for i in range(5, 0, -1):
    for j in range(i):
        print(j, end=" ")
    print()


for i in range(5, 0, -1):
    for j in range(1,i+1):
        print(j, end=' ')
    print()

#Uppercase Row printing
for i in range(5, 0, -1):
    for j in range(0,i):
        print(chr(i+64), end=' ')
    print()
            


    
    
