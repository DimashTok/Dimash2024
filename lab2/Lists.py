mylist = ["apple", "banana", "cherry"]

#Lists are created using square brackets:
thislist = ["apple", "banana", "cherry"]
print(thislist)

"""
List items are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc.
Ordered
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
If you add new items to a list, the new items will be placed at the end of the list.
Changeable
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
Allow Duplicates
Since lists are indexed, lists can have items with the same value:
"""
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


#List Length
#To determine how many items a list has, use the len() function:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))    #Answer 3


#List items can be of any data type:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)


#A list can contain different data types:
list1 = ["abc", 34, True, 40, "male"]
print(list1)

#From Python's perspective, lists are defined as objects with the data type 'list':
#<class 'list'>

mylist = ["apple", "banana", "cherry"]
print(type(mylist))     #Answer <class 'list'>


#It is also possible to use the list() constructor when creating a new list.
thislist = list(("apple", "banana", "cherry"))
print(thislist)


"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#List items are indexed and you can access them by referring to the index number:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])  #Answer banana


#Negative indexing means start from the end
#-1 refers to the last item, -2 refers to the second last item etc.
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])     #Answer cherry


#You can specify a range of indexes by specifying where to start and where to end the range.
#When specifying a range, the return value will be a new list with the specified items.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])    #Answer ['cherry', 'orange', 'kiwi']


#By leaving out the start value, the range will start at the first item:
#This example returns the items from the beginning to, but NOT including, "kiwi":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])     #Answer ['apple', 'banana', 'cherry', 'orange']


#By leaving out the end value, the range will go on to the end of the list:
#This example returns the items from "cherry" to the end:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])     #Answer ['cherry', 'orange', 'kiwi', 'melon', 'mango']


#Range of Negative Indexes
#Specify negative indexes if you want to start the search from the end of the list:
#This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])  #Answer ['orange', 'kiwi', 'melon']


#Check if Item Exists
#To determine if a specified item is present in a list use the in keyword:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")   #Answer Yes, 'apple' is in the fruits list

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#Change Item Value
#To change the value of a specific item, refer to the index number:
#Change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)     #Answer ['apple', 'blackcurrant', 'cherry']


#Change a Range of Item Values
#To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:
#Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)     #Answer ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']


#If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
#Change the second value by replacing it with two new values:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)     #Answer ['apple', 'blackcurrant', 'watermelon', 'cherry']

#Note: The length of the list will change when the number of items inserted does not match the number of items replaced.


#If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
#Change the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)     #Answer ['apple', 'watermelon']


#To insert a new list item, without replacing any of the existing values, we can use the insert() method.
#The insert() method inserts an item at the specified index:
#Insert "watermelon" as the third item:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)     #Answer ['apple', 'banana', 'watermelon', 'cherry']

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#Add List Items

#Append Items
#To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)     #Answer ['apple', 'banana', 'cherry', 'orange']


#Insert Items
#To insert a list item at a specified index, use the insert() method.
#The insert() method inserts an item at the specified index:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)     #Answer ['apple', 'orange', 'banana', 'cherry']


#Extend List
#To append elements from another list to the current list, use the extend() method.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)     #Answer ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']


#Add Any Iterable
#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)     #Answer ['apple', 'banana', 'cherry', 'kiwi', 'orange']

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#Remove List Items

#Remove Specified Item
#The remove() method removes the specified item.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)     #Answer ['apple', 'cherry']

#If there are more than one item with the specified value, the remove() method removes the first occurance:
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)     #Answer ['apple', 'cherry', 'banana', 'kiwi']


#Remove Specified Index
#The pop() method removes the specified index.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)     #Answer['apple', 'cherry']


#If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)     #Answer ['apple', 'banana']


#The del keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)     #Answer ['banana', 'cherry']


#The del keyword can also delete the list completely.
thislist = ["apple", "banana", "cherry"]
del thislist


#Clear the List
#The clear() method empties the list. The list still remains, but it has no content.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)     #Answer []

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#Loop Lists

#Loop Through a List
#You can loop through the list items by using a for loop:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
"""
Answer 
apple
banana
cherry
"""  


#Loop Through the Index Numbers 
#You can also loop through the list items by referring to their index number. Use the range() and len() functions to create a suitable iterable.
#Print all items by referring to their index number:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])    
"""
Answer
apple
banana
cherry
"""  


#Using a While Loop
#You can loop through the list items by using a while loop.
#Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.
#Remember to increase the index by 1 after each iteration.
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

"""
Answer
apple
banana
cherry
"""

#Looping Using List Comprehension
#List Comprehension offers the shortest syntax for looping through lists:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

"""
Answer
apple
banana
cherry
"""

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#List Comprehension
#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

#Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
#Without list comprehension you will have to write a for statement with a conditional test inside:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)      #Answer ['apple', 'banana', 'mango']

#With list comprehension you can do all that with only one line of code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)      #Answer ['apple', 'banana', 'mango']

#The Syntax
#newlist = [expression for item in iterable if condition == True]

#Condition
#The condition is like a filter that only accepts the items that valuate to True.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)      #Answer ['banana', 'cherry', 'kiwi', 'mango']
#The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".


#The condition is optional and can be omitted:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)      #Answer ['apple', 'banana', 'cherry', 'kiwi', 'mango']

#Iterable
#The iterable can be any iterable object, like a list, tuple, set etc.
#You can use the range() function to create an iterable:
newlist = [x for x in range(10)]
print(newlist)      #Answer [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Accept only numbers lower than 5:
newlist = [x for x in range(10) if x < 5]
print(newlist)      #Answer [0, 1, 2, 3, 4]

#Expression
#The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:
#Set the values in the new list to upper case:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)      #Answer ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO'] 

#You can set the outcome to whatever you like:
#Set all values in the new list to 'hello':
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)          #Answer ['hello', 'hello', 'hello', 'hello', 'hello']


#The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)      #Answer ['apple', 'orange', 'cherry', 'kiwi', 'mango']

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#Sort Lists
#Sort List Alphanumerically
#List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)     #Answer ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)     #Answer [23, 50, 65, 82, 100]


#Sort Descending
#To sort descending, use the keyword argument reverse = True:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)     #Answer ['pineapple', 'orange', 'mango', 'kiwi', 'banana']

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)     #Answer [100, 82, 65, 50, 23]


#Customize Sort Function
#You can also customize your own function by using the keyword argument key = function. The function will return a number that will be used to sort the list (the lowest number first):
#Sort the list based on how close the number is to 50:
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)     #Answer [50, 65, 23, 82, 100]


#Case Insensitive Sort
#By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)     #Answer ['Kiwi', 'Orange', 'banana', 'cherry']

#Luckily we can use built-in functions as key functions when sorting a list.
#So if you want a case-insensitive sort function, use str.lower as a key function:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)     #Answer ['banana', 'cherry', 'Kiwi', 'Orange']


#Reverse Order
#What if you want to reverse the order of a list, regardless of the alphabet?
#The reverse() method reverses the current sorting order of the elements.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)     #Answer ['cherry', 'Kiwi', 'Orange', 'banana']

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#Copy a List
#You cannot copy a list simply by typing list2 = list1,
#because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
#There are ways to make a copy, one way is to use the built-in List method copy().
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)       #Answer ['apple', 'banana', 'cherry']


#Another way to make a copy is to use the built-in method list().
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)       #Answer ['apple', 'banana', 'cherry']

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#Join Two Lists
#There are several ways to join, or concatenate, two or more lists in Python.
#One of the easiest ways are by using the + operator.
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)        #Answer ['a', 'b', 'c', 1, 2, 3]

#Another way to join two lists is by appending all the items from list2 into list1, one by one:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)        #Answer ['a', 'b', 'c', 1, 2, 3]

#Or you can use the extend() method, where the purpose is to add elements from one list to another list:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)        #Answer ['a', 'b', 'c', 1, 2, 3]

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#List Methods

"""
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
"""

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
