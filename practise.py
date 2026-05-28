userInput= int(input("Enter your Number to find is it prime or not :-"))
count=0
for i in range(1,userInput+1):
    if userInput % i ==0:
        count=count +1

if(count == 2):
    print(" prime number")
else:
    print("composite number ")