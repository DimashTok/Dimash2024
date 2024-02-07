
#Ex1 
class StringManipulator:
    def __init__(self):
        self.string = ""
    def getString(self):
        self.string = input()
    def printString(self):
        print(self.string.upper())
s=StringManipulator()
s.getString()
s.printString()

#Ex2
class Shape:
    def area(self):
        print('hi')
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        print(self.length ** 2)
shape = Shape()
shape.area()

#Ex3
class Shape:
    def area(self):
        print('hi')

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        print(area)
rectangle = Rectangle(4, 6)
rectangle.area()

#Ex4
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x, self.y)
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    def dist(self, other_point):
        distance = math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
        return distance

#Ex5
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(amount, self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print('hi')
        else:
            self.balance -= amount
            print(amount, self.balance)

#Ex6
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print("Простые числа в списке:", prime_numbers)

