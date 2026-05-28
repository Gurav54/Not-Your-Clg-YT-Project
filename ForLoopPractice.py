#Task 1: print 1 to 20 numbers
number=int(input("Enter your Number :-"))
for i in range(1,number+1):
    print(i)

#Task 2 : print even numbers form 1 to N
askingNumber=int(input("ENTER NUMBER AND GET EVEN NUMBER:-"))
for i in range(1,askingNumber+1):
    if i % 2==0:
        print(i)

#Task 3 : print odd number form 1 to N
askingNum=int(input("Enter number to print odd numbers form it :-"))
for i in range(1, askingNum+1):
    if i % 2!=0:
        print(i)

#Task 4. Print multiplication table of any number
givenNum=int(input("Enter number for multiplication"))
for i in range(1,11):
    print(f"{givenNum} x {i} = {givenNum*i}")

#Task 5. Sum of Nth natural number
sum=0
givenNumber=int(input("Enter your NUMBER SIR :-"))
for i in range(1,givenNumber+1,1):
    sum=sum+i
print(f"sum is ={sum}")

#Task 6. count how many char in word
word=input("Enter your word for printing cha using for loop")
for i in range(len(word)):
    print(word[i])

#Task 7 : print each char + its index
word=input("Enter your word for printing index + char")
for i in range(len(word)):
    print (f"{i} = {word[i]}")

#Task8 : find factorial of give number # HELP TAKEN CHAT-GPT
number=int(input("Enter your number for finding factorial:-"))
factorial=1
for i in range(number,0,-1):
    factorial = factorial * i
print(factorial)

# TASK 9 : Break when number is divisible by 7
userInput=int (input("ENTER NUMBER to check its divisible"))
uptorange =int (input("Enter number  up to you have to calculate the divisiblity :- "))
for i in range(1,uptorange+1,1):
    if i % userInput ==0:
        print(f"here is the number {i} that divisible by {userInput}")


#Task 10 : print vovels form string 
userString=input("Enter your string to find vovels form it :-")
for i in range(len(userString)):
    if userString[i] == 'a' or  userString[i] =='e' or userString[i] == 'i' or  userString[i] =='o' or userString[i]=='u' or userString[i] == 'A' or  userString[i] =='E' or userString[i] == 'I' or  userString[i] =='O' or userString[i]=='U':
#### optimized version of chatgpt :if userString[i] in "aeiouAEIOU":
        print(f"in your string on this position {i} i found vovel and the vovel char is {userString[i]}")

#Task 11: 
# If number is grater then 0 print positive ,if number is less then zero print negetive if number is 0 print zero 

num=int(input("ENTER YOUR NUMBER :-"))
if num == 0:
    print("zero")
elif num > 0:
    print("Positive")
else:
    print("negetive")

#Task 12: Print only constants , remove vowels
userInput=input("Enter your String to remove vowels and print only constants")
for i in range(len(userInput)):
    if userInput[i]  not in ("Aeiouaeiou"):
        print(userInput[i])
    
    userInput = input("Enter your string: ")

#Task 13 : # Break the loop where user sends his digit the loop should run upto 10
digit=int(input("Enter the number :-"))
for i in range(1,11):
    if i == digit:
        break
    else:
        print(i)

#Task 14 : # write a program where loop runs upto 10 and skip 6

skipdigit=int(input("Enter your skipping digit :-"))
for i in range(1,11):
    if i == skipdigit:
        continue
    print(i)

#Task 15 : # write a program where loop runs upto 10 and skip 6

skipdigit=int(input("Enter your skipping digit :-"))
for i in range(1,11):
    if i == skipdigit:
        break
    print(i)


#Task 16 : Write a program that calculates and prints the total sum of all numbers from 1 to 5.
# Expected Output: 15 (because 1 + 2 + 3 + 4 + 5 = 15). 
userInput=int(input("Enter your number here :-"))
total=0
for i in range(1,userInput+1):
    total=total+i
print(total)

#Task 17 : print both evenSum and oddsum 
count=int(input("Enter your for loop range number:-"))
evenSum=0
oddSum=0
for i in range(1,count+1):
    if i%2==0:
        evenSum=evenSum+i
    else:
        oddSum=oddSum+i
print("evenSum ",evenSum)
print("oddSum " ,oddSum)


#Task 18 : find Factors of given number
inputNum=int(input("Enter your Number for finding factor :-"))
for i in range(1,inputNum+1):
    if inputNum %i==0:
        print(i)

#Task 19 :perfect number
userInput=int(input("Enter number:-"))
temp=0
for i in range(1,userInput):
    if userInput % i  ==0:
        temp=temp+i   

if userInput == temp:
    print("Perfect Number")
else:
    print("Not a perfect number")

#Task 20 : prime number OR Composite number
userInput= int(input("Enter your Number to find is it prime or not :-"))
count=0
for i in range(1,userInput+1):
    if userInput % i ==0:
        count=count +1

if(count == 2):
    print(" prime number")
else:
    print("composite number ")