### SET { } ###
""" 
1. A set automatically removes duplicate elemets from setOfData
-> How set do that set work on Hash value of each new element and if same element appered then it will remove it 
duplicates are ignored

2.Unordered: There is no fixed order; items may appear differently every time❌

3.Unindexed: Because they are unordered, you cannot refer to items by an index like myset[0]❌

4.Mutable: You can add or remove items after the set is created.
using its add(new element) method =s.add(40)
---------------------------------------------------------------------------------
5.Heterogeneous in nature  : you can store anything at anytime in set 
BUT : when you do  ->  ❌ Fails: Adding Mutable Elements like a list , 
                       if u store list in set then immediately when u run code then face error 
                       TypeError: cannot use 'list' as a set element (unhashable type: 'list')

                   example :    setData = {1, 2, [3, 4]}  # Lists are mutable

Working : You can safely add strings, numbers, or tuples because 
          their values cannot be modified after creation.
 # This works perfectly
valid_set = {"apple", 42, (1, 2, 3)} 
print(valid_set)
# Output: {42, 'apple', (1, 2, 3)}
-----------------------------------------------------------------------------------
6. You cant replace any current stored value to new value 
( if we have stored RED , BLUE ,WHITE COLORS in set and we have to remove red and add green then 
1st we have to remove red then use add method to add green  )

       # 1. The set itself IS mutable (We can add to it)
            colors = {"red", "blue"}
            colors.add("green")  # Works! The set changed.

            # 2. The items inside MUST BE immutable
            #  You cannot go inside the set and change the string "red" into "ruby".
            # You can only remove "red" and add "ruby".
            colors.remove("red")
            colors.add("ruby")
----------------------------------------------------------------------------------------
7. ⚠️ The Tuple ExceptionA tuple is usually immutable, 
but it can hold mutable items (like a list). If a tuple contains a list, it cannot be added to a set.

# Valid tuple (all items immutable)
good_tuple = (1, 2, 3)
set_a = {good_tuple}  # Works fine

# Invalid tuple (contains a mutable list)
bad_tuple = (1, 2, [3, 4])
try:
    set_b = {bad_tuple}  # Fails!
except TypeError as e:
    print(f"Error: {e}")  # Output: Error: unhashable type: 'list'

----------------------------------------
8. The Empty Set Trap {}
You cannot create an empty set using a = {}. Python reads {} as an empty dictionary.
 if u check its type then the python gives you the type as a dictionary not SET 

 SOLUTION : If u want to create empty SET :
 -> mySet=set() #  (The only correct way to make an empty set)

 --------------------------------------
 9. ❌ What you CANNOT do
 ->You cannot grab a specific item by its index a[i] like a list.

 solution : How you DO access items in a set -> 1. Use a for loop to look at every item
 
      setOfData = {"apple", "banana", "cherry"}
        for item in setOfData:
            print(item)

"""

# Methods of SET {}
# 1. ADD (NEW UNIQUE ELEMENT)
setOfData={1,2,3}
setOfData.add(4)
print(setOfData)

# 2. CLEAR() :remove all elemets 
setOfData.clear()
print(f"2.After using  clear method: {setOfData}") 
# This will remianed set because 1st we created a et with data then we clear the data thats why
#  its not considered as a dictionary 


# 3. discard(elemet that we have to rmeove) : remove any specific element then pass that element in this method
set2Data={11,22,33,44,55}
set2Data.discard(22)
print(set2Data)

# 4. POP() : it will remove random element from set , it will RETURN THAT poped element as well
set3Data={1,3,13,44,22,323}
returnedElement=set3Data.pop()
print(f"Poped element from set ={returnedElement} , After pop() set of data is {set3Data}")

##### ADVANCE METHODS OF SET{ }######

# 5. Difference (difference() or -)
# Difference means:
# Get the elements that are present in the first set
# but NOT present in the second set.
'''
 so if we have two sets s1 and s2 and those having some same elemnts and then we have to get the 
 diference between them then we can use this difference( ) or - 
 '''
 # Example : In below sets in s1 the 3 and 4 is difference elements so wehave to extract them 
 #           then we have to use the difference method on s1 and pass s2 in args 
s1 = {1, 2, 3, 4}
s2 = {11, 22, 1, 2}

# Elements 3 and 4 are only in s1
print(s1.difference(s2))   # Output: {3, 4}

# The - operator does the same thing
print(s1 - s2)             # Output: {3, 4}

#-----------------------------------------------------------------------------------------

# 7. difference_update() or -=

# difference_update() removes all elements from the first set
# that are also present in the second set.
#
# Unlike difference(), it modifies the original set directly.
# so this time we are not just retriving the difference we are modifing the set elements as well
# It updates (changes) the original set directly.

# Example 1st : using  difference_update()
s1 = {11, 21, 31, 41}
s2 = {11, 21, 11, 22}

s1.difference_update(s2)

print(s1)   # Output: {3, 4}
# Example 2nd using -=
s1={10,20,30,40}
s2={90,80,10,20}

s1-=s2
# SO which ever elements are matched between s1 and s2 will be removed 
print(s1)
#---------------------------------------------------------------------------------

# 8.Intersection 
# So the intersection will give us the common elements between both sets 
s1={11,22,111,222}
s2={111,29,20,22}
print( s1.intersection(s2))

#--------------------------------------------------------

# 9. Intersection update ( ) OR &=
# SO the intersection_update method will use to find common elemnts and remove the uncommon elements from s1 set 
# we have alternative two options 1.intersection_update And 2. &=

# Example 1 using intersection_update method 
s1={101,11,21,23}
s2={101,32,22,11}
s1.intersection_update(s2)
print(s1)

# Example 2 using &=
s1={33,44,22,11}
s2={99,88,11,22}
s2 &= s1
print(s2) # so the s2 will ramined with common elements 11 , 22 other elemsnt which are not matched with s1 will removed

#---------------------------------------------

# 10. issubset() or <=

# A set is a subset if all its elements are present in another set. AND this return the BOOL value

s1 = {1, 2, 3}
s2 = {1, 2, 3, 4}
s3={1,2,10}

print(s1.issubset(s2))  # True
#For a set to be a subset, every element of the first set must be present in the second set.
print(s3 <= s2)         # False

#------------------------------------------------

# 11. symmetric_difference() or ^

# Symmetric difference returns the elements which are uncomman in both sets 
# we have two ways to use it 1. symmetric_difference method and 2. ^
s1 = {1, 2, 3, 4}
s2 = {1, 2, 11, 22}

print(s1.symmetric_difference(s2))  # {3, 4, 11, 22}
print(s1 ^ s2)                      # {3, 4, 11, 22}

# If you do below thing then in  s1 set all values are stored in s1 set ={3,4,22,11}
#s1^= s2

#-------------------------------

#12. UNION 
# if you want all values form s1 and s2 as well then we have to use union method 
# we have two options here 1.union() 2. | 

s1={11,22,111,333}
s2={32,31}

print(s1.union(s2))
print(s1 | s2)
