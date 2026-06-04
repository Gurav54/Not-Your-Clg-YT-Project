# list is a data type in python 
##### feature of LIST 
'''
1.Mutable 
2.Duplicate allow 
3.heterogeneous list ( store any kind of data in single list (string int flot etc ))


'''
# 1 MUTABLE NATURE - you can modify or change any values from your list 
l=[10,20,100,200,300]
l[1]=222
print(l) # [10, 222, 100, 200, 300]

# 2 DUPLICATION IS ALLOW : duplicate data will be allowed in list 
listobj=[1 ,1,2,2,1,1,3,3,3]
print(listobj) # [1, 1, 2, 2, 1, 1, 3, 3, 3]

#How to access the elements form list 
fruits=["Banana", "Mango","Apple","Orange"]
print(fruits[0])
print(fruits[-2])
print(fruits[0:2])
print(fruits[-3:-1]) # This is slicing where we started the slicing from mango upto Ornage so op : Mango and APPLE 
#❌ Start on the right, end on the left
print(fruits[-1:-3]) # WHY this list is getting empty [] because Python tries to move forward (default behavior), but -3 is behind Orange.Orange -> ??? (moving forward) It can never reach -3, so:
# BELOW IS THE SOLUTION FOR ABOVE EMPTY LIST 
print(fruits[-1:-3:-1]) # WE HAVE specifed that you have to walk backword -1 

fruits[3]="Kandamula" # Modification is allowed so replaced the Orange -> Kandamula
print(fruits)

# if you want to add new element in existing list we have append method 
# METHOD OF LIST 1. Append
fruits.append("Gajar")
print(f"After using append method {fruits}")

### Travesing a list elements
#1.printing direct list 
mylist=[10,20,30,40,111,111,111,1]
print(mylist)
#2.Printing one by one elements form list 
for i in mylist:
    print(i)
#3 travesing list using index
for i in range(0,len(mylist)):
    print(f"{mylist[i]}")


### 3. A natural heterogeneous list in Python
myylist = [42, "Hello", 3.14, True]
print(myylist)

## Methods for list 
# 1. append  -> the append method will add new element at last in list 
digits=[1,1,2,3,4,42,1,2]
digits.append(55)
print(digits)

#2. insert(index , new element) -> let say you have to add new element at any position then we will use insert method 
# it will accept the new element and index number where you want to insert new element 

numbers=[1,2,3,2,1,2,312]
numbers.insert(0 , 1111111)
print(numbers)

# :: so for creating new element you have two methods 1.append 2.insert 


#3. DELETE  -> FOR DELETING ANY ELEMENT FROM LIST WE HAVE 2-3 METHODS 
# REMOVE () | POP() | CLEAR()

#POP()
# The POP(INDEX OR EMPTY) the pop method will accept the index number based on index number it will delete that value 
 #OR else if you just pass object.pop() empty then last number will be removed
 # by using pop we can return the poped value from list , which ever element is removed we will get that element
 # Error : if we pass invaild index then we will face error = IndexError (if index out of bounds)
numberList=[1,2,3,4,5]
numberList.pop(0) # pass the index value if u not pass the index value LAST VALUE will be Automatically removed
poped=numberList.pop() # lastvalue means 5 will be removed 
print(f"poped element is ={poped}")
print(numberList)

#REMOVE()
#The remove method will accept the value in parameter , and if the same value occured multiple times 
 # then 1st occured value will removed other same values remained in list
 # Error : what ever value we pass and thatvalue is not present in list then we will get the value error : ValueError (if item not found)
listOfData=[11,22,33,4,5,11,7,11]
listOfData.remove(11)
print(listOfData)

#CLEAR()
# when ever you want to delete all elements then use clear(), the list will be empty at last when you use this method 
# No error : while the list is empty and we use clear method on empty list then we will not face error so its fine 
listFromClear=[11,22,33,44,55,77]
listFromClear.clear()
print(listFromClear)


#SORT ()
listdata=[1,33,2,4,22,322,8]
# We can sort list in Asending order or in desending order as well
# By default its Asending order , you can mention also but due to its default naturel we will get listdata in asending order 
listdata.sort()
print(f"sorted default list{listdata}")
# sort list in desending order we have to pass parameter as reverse= True
listdata.sort(reverse=True)
print(f"sorted list in desending order ,reverse = True {listdata}")
# sort list in Asending order using reverse=False
listdata.sort(reverse=False)
print(f"Asending order for list using reverse=False{listdata}")


#REVERSE ()
# When you want to reverse any data use reverse()
listofdataa=[1,33,2221,12,112,3422]
listofdataa.reverse()
print(f"Normal reversed the list data {listofdataa}")
