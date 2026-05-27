
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
a="Apple"
for i in a:
    print (i)

# For loop , getting String form user and print it 
name=input("Enter your Name")

for i in range(len(name)):
    print(f"{i} : {name[i]}")