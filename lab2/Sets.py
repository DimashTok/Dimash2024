#Set
#Sets are used to store multiple items in a single variable.
myset = {"apple", "banana", "cherry"}
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Set Items
#Set items are unordered, unchangeable, and do not allow duplicate values.

#Unordered
#Unordered means that the items in a set do not have a defined order.
#Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

#Unchangeable
#Set items are unchangeable, meaning that we cannot change the items after the set has been created.

#Once a set is created, you cannot change its items, but you can remove items and add new items.

#Duplicates Not Allowed
#Sets cannot have two items with the same value.
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

#The values True and 1 are considered the same value in sets, and are treated as duplicates:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

#The values False and 0 are considered the same value in sets, and are treated as duplicates:
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

#To determine how many items a set has, use the len() function.
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#Set items can be of any data type:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#A set can contain different data types:
set1 = {"abc", 34, True, 40, "male"}

#From Python's perspective, sets are defined as objects with the data type 'set': <class 'set'>
myset = {"apple", "banana", "cherry"}
print(type(myset))

#It is also possible to use the set() constructor to make a set.
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#Access Items
#You cannot access items in a set by referring to an index or a key.
#But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

#To add one item to a set use the add() method.
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#To add items from another set into the current set, use the update() method.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#Remove Item
#To remove an item in a set, use the remove(), or the discard() method.
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

#If the item to remove does not exist, remove() will raise an error.

#Remove "banana" by using the discard() method:
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
#If the item to remove does not exist, discard() will NOT raise an error.

#You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
#The return value of the pop() method is the removed item.
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
#Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

#The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#Loop Items
#You can loop through the set items by using a for loop:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#Join Two Sets
#There are several ways to join two or more sets in Python.
#You can use the union() method that returns a new set containing all items from both sets, 
#or the update() method that inserts all the items from one set into another:

#The union() method returns a new set with all items from both sets:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

#The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

#Both union() and update() will exclude any duplicate items.

#Keep ONLY the Duplicates
#The intersection_update() method will keep only the items that are present in both sets.

#Keep the items that exist in both set x, and set y: 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

#The intersection() method will return a new set, that only contains the items that are present in both sets.
#Return a set that contains the items that exist in both set x, and set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

#Keep All, But NOT the Duplicates
#The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

#The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

#True and 1 is considered the same value:
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}
z = x.symmetric_difference(y)
print(z)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#Set Methods
#Python has a set of built-in methods that you can use on sets.

#add()	Adds an element to the set
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)

#clear()	Removes all the elements from the set
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)

#copy()	Returns a copy of the set
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)

#difference()	Returns a set containing the difference between two or more sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)

#difference_update()	Removes the items in this set that are also included in another, specified set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)

#discard()	Remove the specified item
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)

#intersection()	Returns a set, that is the intersection of two other sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

#intersection_update()	Removes the items in this set that are not present in other, specified set(s)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

#isdisjoint()	Returns whether two sets have a intersection or not
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)

#issubset()	Returns whether another set contains this set or not
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

#issuperset()	Returns whether this set contains another set or not
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)

#pop()	Removes an element from the set
fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)

#remove()	Removes the specified element
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)

#symmetric_difference()	Returns a set with the symmetric differences of two sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

#symmetric_difference_update()	inserts the symmetric differences from this set and another 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

#union()	Return a set containing the union of sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)

#update()	Update the set with the union of this set and others
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x)