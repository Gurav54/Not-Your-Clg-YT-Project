# 1. print string using forloop 
"""
userInput=input("Enter your String ")
rev=""
for i in range(len(userInput)-1,-1,-1):
    rev= rev+userInput[i]
print(rev)
"""

# 2 String palindrome  
"""
userInput=input("Enter your String to check is it palindrome  or not ")
rev=""
for i in range(len(userInput)-1,-1,-1):
    rev= rev+userInput[i]
print(rev)
if rev == userInput:
    print(f"The string you passed is palindrome  string {userInput}")
else:
    print(f"String you passed is not a palindrome  string{userInput}")
"""

#3 print the count of digits | special chars | char count seprate 
"""

givenString="abcd123@3$aby"
digitsCount=0
spCharCount=0
charCount=0

for i in givenString:
    if i.isdigit():
        digitsCount=digitsCount+1
    elif i.isalpha():
        charCount=charCount+1
    else :
        spCharCount=spCharCount+1

print(f"your char count is = {charCount} | Your special char count is ={spCharCount} | Your digits count is ={digitsCount}")

"""

# 4 print the digits | char | special chars from string seprate
"""

inputString="abcd123@3$aby"
digits=""
chars=""
spChars=""
for i in inputString:
    if i.isdigit():   
        digits=digits+i
    elif i.isalpha():
        chars=chars+i
    else:
        spChars=spChars+i
    
print(f"char form givien string :-{chars}")
print(f"sp chars form givien string :-{spChars}")
print(f"digits form givien string :-{digits}")


"""
# ORD values assic values 
# 0-9 = 48 to 57
# a-z = 97 to 122
# A-Z = 65 to 90    

inputString="abcd123@3S$DabDyA"
digitsCount=0
spCharCount=0
lowercharCount=0
uppercharCount=0
allChars=0
for i in inputString:
    if (ord(i) >=65 and  ord(i) <=90) :
        uppercharCount=uppercharCount+1
        allChars=allChars+1
    elif(ord(i)>=48 and ord(i)<=57):
        digitsCount=digitsCount+1
    elif(ord(i)>=97 and ord(i)<=122):
        lowercharCount=lowercharCount+1
        allChars=allChars+1
    else:
        spCharCount=spCharCount+1
print(f"ALL CHAR COUNT {allChars}")
print(f"small  CHAR COUNT {lowercharCount}")
print(f"captital CHAR COUNT {uppercharCount}")
print(f"digits  COUNT {digitsCount}")
print(f"special char COUNT {spCharCount}")



    