
# range ( starting , ending+1 ,steps)
# range(starting from 1 ,ending on 10 so 11 , step one by one so 1)

#its not mandatory to pass all three parameters but the ending should be there 
#range(46) # so the loop will goes upto 45 

# Print the 5th table   
"""
for i in range (5 ,51,5):
    print(i)
"""

# write a code where accept input form user and print that table 
"""
input=int(input("Enter your table number :-"))
for i in range (input ,(input*10)+1 ,input):
    print(i)

"""

# For loop on single string 
"""
a="Apple"
for i in a:
    print (i)
"""

# For loop , getting String form user and print it 
"""
name=input("Enter your Name")

for i in range(len(name)):
    print(f"{i} : {name[i]}")
 """

#### For loop , BREAK | CONTINUE | ELSE #######

# For loop break example 
for i in range (1,11,1):
    if i == 5:
        break
    print(i)

for i in range(1,11,1):
    if i ==6:
        continue
    print(i)

# ELSE in For loop
#The else block runs only if the loop finishes entirely without hitting a break.

for i in range(1,21,1):
    if i == 69:
        break
    print(i)
else:
    print("FOR LOOPS didnt Hit break statement")

#Task 1 : Print Hello world nth time 
inputFromUser=int(input("Enter how many time you want to print Hello world:-"))
for i in range(1,inputFromUser+1,1):
    print(f"{i} Hello World")

# Task 2 : print natural numbers based on N th value 
givenNumber=int(input ("Enter your number :-"))
for i in range(1,givenNumber+1):
    print(i)

# Task 3 : print the numbers in reverse order , get input from user 
number=int (input("Enter your Number for reverse printing :-"))
for i in range(number , 0,-1):
    print(i)

#Task 4 : print the 5th table , output should be 5x1=5 , 5x2=10 ....

number=int(input("Enter your Number for table print :-"))
for i in range(1,11,1):
    print(f"{number} x {i}={number*i}")
    #print(number*i)

#Task 5 : print the addition of natural numbers
number=int(input("Enter your number for addition :-"))
sum=0
for i in range(1,number+1):
    sum=i+number
print(sum)