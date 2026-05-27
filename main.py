#print("Hello, World!")

a=" my self Akash"
print(a[8:14])

#step by step slicing  # Output : Dstp
b="Desktop"
print(b[0:7:2]) # Strating position : 0, Ending position : 7, Step : 2

# Task : Print "Python" from the string "I am learning Python Programming"
c="I am learning Python Programming"
print(c[14:20])
print(c[14:20:1])

print(c[-18:-12])


## Type conversion
x="10"
x=int(x)
print(type(x) , "Value of x is =",x+5)

y=10.5
print(type(y) , " before type conversion, Value of y is =",y)
y=int(y)
print(type(y) , " After type conversion, Value of y is =",y)
y=str(y)
print(type(y), "The value of Y after converting to string is =",y)

# type conversion using BOOL
a=0
b=11
c=-5
d=0.0
e=0.0001
f=" "
g=""
h="Hello"
xxx="0"
print(a,"-->",bool(a)) # Output : False
print(b,"-->",bool(b)) # Output : True  
print(c,"-->",bool(c)) # Output : True
print(d,"-->",bool(d)) # Output : False
print(e,"-->",bool(e)) # Output : True
print(f,"-->",bool(f)) # Output : True
print(g,"-->",bool(g)) # Output : False
print(h,"-->",bool(h)) # Output : True
print(xxx,"-->",bool(xxx)) # Output : True , because any non-empty string is considered True in boolean context
 
## Expilicit type conversion
x=10
y=x/2
print(type(y), "Value of y is =",y)


### lecture 5 Input and output & opretions
# 1 printing techniques 
name=" Shadow"
age=25
# using f string to print the output  , f means format string
print(f"My name is{name} and my current age is {age}")
#normal concatenation way to print  same output
print('my name is',name , 'and my age is' ,age)


## Input function , for getting the input from the user 
a=input("whats your age :-")
print(type(a)) # Output : <class 'str'> , because input function always return string value

b=int(input("whats your age :-"))
print(type(b)) # Output : <class 'int'> , because we have converted the string value to integer using int() function

print(f"your age is {b}")

## Flore devision
x=10
y=3
print(x/y) # Output : 3.3333333333333335
print(x//y) # Output : 3 , it will revome the decimal part and give the integer value as output


## power opretion
print(4*2) # Output : 8
print(4**2) # Output : 16 , it will give the power of the number


#comparison opretion
print (12>14) # Output : False

#logical opretion
print(12<14 and 14>10 and 10==7)
 # Output : False , because 10 is not equal to 7
print(12<14 or 14>10 or 10==10 ) 
# Output : True the or oprator need any one condition to be true to give the output as true and in this case 10 is equal to 10 so it will give the output as true
print(not(12<14)) 
"""
 Output : False because 12 is less than 14 so it will give the 
 output as true BUT we have used not operator so it will give 
 the output as false BECAUSE NOT OPERATOR REVERSE THE OUTPUT
 """

# Task 
print((5>3 and 10==10) or (22 !=22  and 2<1)) # Output : true  OR IS main opretor and the or needs any one condtion true

print ((10==10 and 23!=23) or (32 ==12 and bool("Hello"))) 
#bool("Hello") is TRUE 
#OUTPUT : (TRUE | FALSE ) = FALSE  OR (FALSE | TRUE)= FALSE 
# SO final output is FALSE

print(not(10==10 and 1!=2) or (10>=12))
#output is true 
#TRUE AND TRUE = TRUE [ OR ]  FALSE 
# then final output is  [ TRUE ] BUT 
# we have used NOT OPERATOR so it will give the output as  [[ FALSE ]]
