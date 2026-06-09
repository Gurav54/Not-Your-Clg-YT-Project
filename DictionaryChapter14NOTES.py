### DICTIONARY { } ###
"""
*] Definition  :  Dictionary store the data in Key : value pairs like a json 
                * The Dictionary can store heterogeneous Data 
        Rules  :  1.Key should unique 
                  2.Value can be duplicate , Any 
                  3.value can be accessble using its key   
"""
# Example 1:
dic={
    "1":"Akash",
    "2":"Sumit",
    "3":"Snaket",
    "4":"Big show"
}

print(dic) # {'1': 'Akash', '2': 'Sumit', '3': 'Snaket', '4': 'Big show'}

# CRUD 
# 1(C= CREATING NEW ELEMENT)  ADDING NEW ELEMENTS 
dic["5"] ="Rushi"
dic["Town"] ="Pune"
print(dic)

# 2( R = Read) : pass key init 
 #1st Approach passing key and get value 
print(dic["2"])

 #2nd Approach useing get("pass Key") and get the vlaue 
print(f"After using get() {dic.get("2")}")
 

# 3. UPDATE (Pass Key and assign new Value)
dic["5"] = "Rushikesh"
print(f"After Updating: {dic}")

# 4. DELETE (Pass Key to remove Key-Value Pair)
  # There are two ways to delete 

 #1 : Delete By Key  | delete Any specific key:value
del dic["Town"]
print(f"After Deleting Town: {dic}")

 #2 : Delete or clear whole dictionary
print(dic.clear())

#-----------------------------------------------
# iteam() : this will do the dictionary to list and in that list we will see each key value pair having its own tuple 
#it will retrun the data in LIST 
mDic = {
    "1": "Akash",
    "2": "Sumit",
    "3": "Snaket",
    "4":"sxds"
}

print(mDic.items()) #Op : dict_items([('1', 'Akash'), ('2', 'Sumit'), ('3', 'Snaket')])

#Keys ()
# It will return all keys only  in dictionary

print(mDic.keys()) # Op : dict_keys(['1', '2', '3'])

#values()
#It will return all values only 
print(mDic.values()) #OP :dict_values(['Akash', 'Sumit', 'Snaket'])

#POP()
# Removes the key-value pair for the given key.
# Returns the value that was removed.
popped = mDic.pop("2")
print(popped)

#popIteam()
#it will remove last key-value pair form dictionary

popedItem=mDic.popitem()
print(popedItem)


#setDefault(key : DefaultValue)
#1. If : the key is already exist then it will return its present value 
#    else: the key does not exist in dictionary then , it creates the key with default value AND return that value 

#Example 1: Key already exists
mDic = {
    "1": "Akash",
    "2": "SumitXD"
}

result = mDic.setdefault("2", "Rushikesh")

print(result)
print(mDic)

#Example 2: Key does not exist

myDic2={"1":"Akash","2":"Sumit"}
myDic2.setdefault("3","Rushikesh")

print(myDic2) #OP :{'1': 'Akash', '2': 'Sumit', '3': 'Rushikesh'}

#UPDATE()
#1. IT will just update the given value for that given key 
#   If that key does not exist then it will create new key-value pair

d={"A":"Akash","B":"Boxer","C":"Cars"}
d.update({"A":"Shadow"}) # Key exists so value will be updated 
d.update({"D":"DUDE"})  # key does not exists new key-value pair will be created 

print(d) # OP :{'A': 'Shadow', 'B': 'Boxer', 'C': 'Cars', 'D': 'DUDE'}

print("----------------------------------------------------------------------------------------")

# Traversing Data (LOOPS ON DICTIONARY)
du={"10":"100","20":"200","30":"300"}
for i in du:
    print(f"the key is ->{i} The value is {du[i]}")

####  QUESTIONS #######

#Q1 . MEREGE TWO DICTIONARYS 
d1={"1":"A","2":"B","3":"C"}
d2={"4":"D","5":"E"}

## Quick solution 1. update method 
d1.update(d2)
print(d1) #{'1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E'}

## using forloop

for i in d2:
    d1[i]=d2[i]

print(d1)

#----------------------------------------

#Q2. sum of all values 
dd1={"1":11,"2":1111,"3":111111}
sum=0
for i in dd1:
    sum=sum+dd1[i]

print(sum)