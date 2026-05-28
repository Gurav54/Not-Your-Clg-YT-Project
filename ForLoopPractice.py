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
