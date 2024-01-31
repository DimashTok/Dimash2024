print(10 > 9)  #Answer True
print(10 == 9) #Answer Flase
print(10 < 9)  #Answer False

#When you run a condition in an if statement, Python returns True or False.
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print(bool("Hello")) #Answer True
print(bool(15))      #Answer True

x = "Hello"
y = 15
print(bool(x)) #Answer True
print(bool(y)) #Answer True

print(bool("abc"))                          #Answer True
print(bool(123))                            #Answer True
print(bool(["apple", "cherry", "banana"]))  #Answer True

print(bool(False))  #Answer Flase
print(bool(None))   #Answer Flase
print(bool(0))      #Answer Flase
print(bool(""))     #Answer Flase
print(bool(()))     #Answer Flase
print(bool([]))     #Answer Flase
print(bool({}))     #Answer Flase

class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))  #Answer Flase

def myFunction() :
  return True
print(myFunction()) #Answer True

def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!") #Answer YES! if the function outputs True otherwise False

x = 200
print(isinstance(x, int)) #check if an object is an integer or not


