#Lists
list =[ "apple","banana","grapes"]

'''
Lists are used to store multiple itmes in a single variable.
Lists are one of the four built-in data types in Python.
Lists are created using square brackets.
'''

#Create a list
list10 = ["apple","banana","grapes"]
print(list10)

'''
Items in a list are ordered,changeable and allow duplicte values
List items are indexed
 
Ordered : items in a list have a defined order, and the order will not change.
If you add new items to a list, the new items will be placed at the end of the list.

Changeable - we can change, add, or remove items in a list after it has been created.

'''
#Allows duplicates
list = ["apple","banana","cherry","grapes","cherry"]
print (list)

#Length 
#len()

print(len(list))

#Data types
list = ["apple",34,True,"male"]
#a list with different values

#Access elements in the list 
print(list[0])
print(list[3])

#Change value
list10[1] = "orange"

#Add elements
list10.append(5) #add at the end 
list10.insert(1, 10)  # add at position

#Extend 
list1 = [1,2]
list2 = [3,4]
list1.extend(list2)

#remove elements
list1.remove(2) #remove value
list1.pop() #remove last
list1.pop(1) #remove index

#Clear list
list10.clear()

#Check element
if "apple" in list10:
    print("Available")


#loop through list
for item in list:
    print(item)

#loop with index 
for i in range(len(list10)):
    print(list10[i])

#sort list
list10.sort()

#reverse list
list10.reverse()

#count elements 
list10.count(2)

#max n min
max(list1)
min(list1)

#slice list 
list10[1:4]

#nested list
matrix =[[1,2],[3,4]]
print(matrix[0][1])

#join lists
list3 = list2+list1

#delete list 
del list10
#multiply list
nums = [1,2,3,4]
print(nums*2)