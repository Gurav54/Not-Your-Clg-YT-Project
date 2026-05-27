## IF ELSE STATEMENT
"""
age=int(input("Enter your age:-"))
if age>=18:
    print("you are eligible for vote")
else:
    print("you are not eligible for vote")
"""

# Nested if else statement Money example
"""
money =int(input("Emter how much money you have:-"))
if money==1000:
    print("i can buy a water bottle")
elif money == 5000:
    print ("i can buy a Headphones")
elif money == 10000:
    print ("i can buy a watch")
elif money < 10000000:
    print("i can buy anything")
else:
    print("i dont want to buy anything")

"""

# Nester if elif else comparing 2 numbers 
"""
num1=int(input("Enter your 1st number:-"))
num2= int(input("Enter your 2nd number :- "))

if num1>num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    print("both numbers are equal")

"""

# if else statement with string Gender example
"""
gender = input("please enter your gender in M or F:-")

if gender =="M" or gender =="m":
    print("Hello sir")
elif gender =="F" or gender =="f":
    print("Hello mam")
else:
    print("Hello le-ZAND")
"""

# if else example with even odd number
"""
a = int(input("Enter your input number :-"))
if(a % 2 ==0):
    print(f"{a} is an even number")
else:
    print(f"{a} is an odd number")

"""
# if else  Age and name example
"""
name =input("Please enter your name :-")
age=int(input("please enter your Age:-"))
if age <= 18 :
    print(f"you are not allow to vote because your age is {age} , sorry {name}")
else:
    print(f"you are valid person , your age is {age} ,please vote {name}")
"""

year=int(input("Enter the year:-"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(" this is leap year")
else:
    print ("This is not a leap year ")