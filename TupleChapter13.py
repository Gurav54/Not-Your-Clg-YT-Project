""" 
TUPLE ( ) :-
Tuple is Data type ,its same as List where the diffrence between LIST and Tuple is ,
in tuple u cant change values (Modification) is not allowed.

A tuple is exactly like a list, except you cannot change it once created. Use tuples for 
data that should stay constant — like days of the week, coordinates, or config values

TUPLE : ORDERED | DUPLICATION ALLOW | ACCESS ELEMENT FORM INDEX | Heterogeneous NATURE
        MODIFICATION IS NOT ALLOWED ❌ 
""" 

# Modifing Tuple to see what Error we get 
#TypeError: 'tuple' object does not support item assignment
'''
firstTuple= (1,2,3,4)
for i in firstTuple:
    firstTuple[i] = 7

print(firstTuple) 
'''

# TUPLE METHODS 
# 1.Index() : this is accept value in parameter and return the INDEX OF that value 
#             if same value present in  TUPLE multiple times it will return the 1st occurence of that value 
#    ERROR : if value is not in TUPLE then we will get : ValueError: tuple.index(x): x not in tuple
digits=(11,22,33,44,55,11)
ret=digits.index(11)
print(ret)



#  | 2.count()
digitsTup=(10,20,30,40,10,90)
x=digitsTup.count(10)
print(x)