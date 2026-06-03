# TYPES OF FUNCTIONS -> ( there are two types of functions user define functions And inbuild functions)
# 1.positional Funtion
# 2.Default Function 
# 3.Key Function

### Basic function created
def myFunctionName(): # created function
    print("Hello World")

myFunctionName() # calling function 

# parameters in functions 

def parameterFunction(a ,b):
    print(a+b)

parameterFunction(10,20)
parameterFunction(41,49)

## 1 Positional function
# In positional function we pass all parameters mandetory , we have to pass all parameter compulsory
# Error -> if u didnt pass any parameter then we will get the error ->

def myPositionalFunction(a,b,c,d):
    print(a+b+c+d)

myPositionalFunction( 10, 1, 2, 3)
#myPositionalFunction(10,1,2) #Error -> TypeError: myPositionalFunction() missing 1 required positional argument: 'd'

#### Default Fuction ####
"""
This is a solution for the error:
TypeError: myPositionalFunction() missing 1 required positional argument: 'd'

How?
By using default arguments in a function. If a value is not passed
for a parameter, Python automatically uses its default value.

Note:
All parameters that have default values should be written at the end
of the parameter list. Otherwise, Python will raise a SyntaxError.

we cant do this : def additionFunction(a=5,b,c=10):
we have to do this def additionFunction(b,a=5,c=10):
"""

def additionFunction(a,b,c=10):
    print(a+b)
    print(a+b+c)

print(10+20) # here we didnt pass the c value so python will accept the default vale which is 10
print(11+12+13) # here we pass all values so that c=10 will not considered 


### 3-> KeyWord argument Function
"""
### 3 -> Keyword Argument Function

In a keyword argument function, values are passed using parameter names.
This makes the code easier to read, and the order of arguments does not matter.

The order of arguments does not matter as long as the parameter names are provided correctly.

"""

def studentFunction(name, age):
    print(name, age)

studentFunction(age=25, name="Akash")

def additionFun(a,b,c):
    print(a+b+c)

additionFun(c=10,a=5,b=3)
additionFun(10,11,12)
#additionFun(10,c=12,11) on this line we will get error because 
# This will give an error because after using a keyword argument,
# we cannot pass a normal (positional) argument , where ever you pass any arg as a keyword Arg then up coming variable also need to pass the keyword arg.