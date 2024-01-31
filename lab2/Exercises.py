#Booleans Ex

# Ex1
print(10>9)     #Answer True

# Ex2
print(10==9)    #Answer False

# Ex3
print (10<9)    #Answer False

# Ex4
print(bool("abc"))  #Answer True

# Ex5
print(bool(0))  #Answer False

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#Operators

#Ex1
print(10*5)     #Answer 50

#Ex2
print(10/2)     #Answe 5

#Ex3
fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")       #Answer Yes, apple is a fruit!

#Ex4
if 5 !=10:
  print("5 and 10 is not equal")        #Answer 5 and 10 is not equal

#Ex5
if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")       #Answer At least one of the statements is true

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#Lists

#Ex1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])        #Answer banana

#Ex2
fruits = ["apple", "banana", "cherry"]
fruits[0]= "kiwi"       
print(fruits)           #Answer ['kiwi', 'banana', 'cherry']

#Ex3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)           #Answer ['apple', 'banana', 'cherry', 'orange']

#Ex4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")
print(fruits)           #Answer ['apple', 'lemon', 'banana', 'cherry']

#Ex5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)           #Answer ['apple', 'cherry']

#Ex6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])       #Answer cherry

#Ex7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])      #Answer ['cherry', 'orange', 'kiwi']

#Ex8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))      #Answer 3

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#Tuple 

#Ex1
fruits = ("apple", "banana", "cherry")
print(fruits[0])        #Answer apple

#Ex2
fruits = ("apple", "banana", "cherry")
print(len(fruits))      #Answer 3

#Ex3
fruits = ("apple", "banana", "cherry")
print(fruits[-1])       #Answer cherry

#Ex4
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])      #Answer ('cherry', 'orange', 'kiwi')

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#Sets

#Ex1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")         #Answer Yes, apple is a fruit!

#Ex2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)                             #Answer {'banana', 'apple', 'orange', 'cherry'}

#Ex3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)                             #Answer {'orange', 'banana', 'grapes', 'cherry', 'apple', 'mango'}

#Ex4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)                             #Answer {'apple', 'cherry'}

#Ex5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)                             #Answer {'apple', 'cherry'}

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#Dictionaries

#Ex1
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))                 #Answer Mustang

#Ex2
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020
print(car)                              #Answer {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

#Ex3
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"
print(car)                              #Answer {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

#Ex4
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car)                              #Answer {'brand': 'Ford', 'year': 1964}

#Ex5
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car)                              #Answer {}

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#If Else

#Ex1
a = 50
b = 10
if a > b :
  print("Hello World")                  #Answer Hello World

#Ex2
a = 50
b = 10
if a != b:
  print("Hello World")                  #Answer Hello World

#Ex3
a = 50
b = 10
if a == b:
  print("Yes")
else:
  print("No")                           #Answer No

#Ex4
a = 50
b = 10
if a == b:
  print("1")
elif a > b:
  print("2")
else:
  print("3")                            #Answer 2

#Ex5
"""
if a == b and c == d:
  print("Hello")  
"""                     

#Ex6
"""
if a == b or c == d:
  print("Hello")   
"""                     

#Ex7
if 5 > 2:
  print("YES")                          #Answer YES

#Ex8
a = 2
b = 5
print("YES") if a == b else print("NO")  #Answer NO

#Ex9
a = 2
b = 50
c = 2
if a == c or b == c:
  print("YES")                          #Answer YES
    
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#While Loops

#Ex1
i = 1
while i < 6:
  print(i)                              
  i += 1

#Ex2
i = 1
while i < 6:
  if i == 3:
    break
  i += 1 

#Ex3
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)                             

#Ex4
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")   

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#For Loops

#Ex1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Ex2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)  

#Ex3
for x in range(6):
  print(x)  

#Ex4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)  

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''