print(10 + 5) #Answer 15

"""
Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators
"""
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#Python Arithmetic Operators
x = 5
y = 3
print(x + y)    #Answer 8

x = 5
y = 3
print(x - y)    #Answer 2

x = 5
y = 3
print(x * y)    #Answer 15

x = 12
y = 3
print(x / y)    #Answer 4

x = 5
y = 2
print(x % y)    #Answer 1

x = 2
y = 5
print(x ** y) #2 to the 5th power 2^5 Answer 32

x = 15
y = 2
print(x // y) #Rounds the result to the nearest number Answer 7

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#Python Assignment Operators
x = 5
print(x)    # x = 5     Answer 5

x = 5
x += 3
print(x)    # x = x + 3 Answer 8

x = 5
x -= 3
print(x)    # x = x - 3 Answer 2

x = 5
x *= 3
print(x)    # x = x * 3 Answer 15

x = 5
x /= 3
print(x)    # x = x / 3 Answer 1.6666666666666667

x = 5
x%=3
print(x)    # x = x % 3 Answer 2

x = 5
x//=3
print(x)    # x = x // 3 Answer 1

x = 5
x **= 3
print(x)    # x = x ** 3 Answer 125

x = 5
x &= 3
print(x)    # x = x & 3 Answer 1

x = 5
x |= 3
print(x)    # x = x | 3 Answer 7

x = 5
x ^= 3
print(x)    # x = x ^ 3 Answer 6

x = 5
x >>= 3
print(x)    # x = x >> 3 Answer 0

x = 5
x <<= 3
print(x)    # x = x << 3 Answer 40

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#Python Comparison Operators
x = 5
y = 3
print(x == y)   #Answer False

x = 5
y = 3
print(x != y)   #Answer True

x = 5
y = 3
print(x > y)    #Answer True

x = 5
y = 3
print(x < y)    #Answer False

x = 5
y = 3
print(x >= y)   #Answer True

x = 5
y = 3
print(x <= y)   #Answer False

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#Python Logical Operators
x = 5
print(x > 3 and x < 10) #returns True because 5 is greater than 3 AND 5 is less than 10
#Answer True

x = 5
print(x > 3 or x < 4) #returns True because one of the conditions is true (5 is greater than 3, but 5 is not less than 4)
#Answer True

x = 5
print(not(x > 3 and x < 10)) #returns False because not is used to reverse the result
#Answer False

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#Python Identity Operators
#i- Returns True if both variables are the same object
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
# returns True because z is the same object as x
print(x is y)
# returns False because x is not the same object as y, even if they have the same content
print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y


#is not-Returns True if both variables are not the same object
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is not z)
# returns False because z is the same object as x
print(x is not y)
# returns True because x is not the same object as y, even if they have the same content
print(x != y)
# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#Python Membership Operators
#in 	Returns True if a sequence with the specified value is present in the object
x = ["apple", "banana"]
print("banana" in x)
# returns True because a sequence with the value "banana" is in the list


#not in	Returns True if a sequence with the specified value is not present in the object
x = ["apple", "banana"]
print("pineapple" not in x)
# returns True because a sequence with the value "pineapple" is not in the list

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#Python Bitwise Operators
#Bitwise operators are used to compare (binary) numbers

print(6 & 3)
#  &   AND	Sets each bit to 1 if both bits are 1	x & y
"""
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
====================
"""

# |	 OR	 Sets each bit to 1 if one of two bits is 1	  x | y
print(6 | 3)
"""
The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
7 = 0000000000000111
====================
"""

#   ^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y
print(6 ^ 3)
"""
The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
5 = 0000000000000101
====================
"""

#  ~  NOT  Inverts all the bits	  ~x
print(~3)
"""
The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).

Inverted 3 becomes -4:
 3 = 0000000000000011
-4 = 1111111111111100
"""

#   <<	Zero fill left shift	 Shift left by pushing zeros in from the right and let the leftmost bits fall off	 x << 2
print(3 << 2)
"""
The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:

If you push 00 in from the left:
 3 = 0000000000000011
becomes
12 = 0000000000001100
"""

#   >>	Signed right shift	   Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	  x >> 2
print(8 >> 2)
"""
The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010
"""

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#Operator Precedence
#Operator precedence describes the order in which operations are performed.
#Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first
print((6 + 3) - (6 + 3)) #Answer 0


#Multiplication * has higher precedence than addition +, and therefor multiplications are evaluated before additions
print(100 + 5 * 3) #Answer 115


#he precedence order is described in the table below, starting with the highest precedence at the top
"""
()	                Parentheses	
**	                Exponentiation	
+x  -x  ~x	        Unary plus, unary minus, and bitwise NOT	
*  /  //  %	        Multiplication, division, floor division, and modulus	
+  -	            Addition and subtraction	
<<  >>	            Bitwise left and right shifts	
&	                Bitwise AND	
^	                Bitwise XOR	
|	                Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	        Comparisons, identity, and membership operators	
not	                Logical NOT	
and	                AND	
or	                OR
"""

#If two operators have the same precedence, the expression is evaluated from left to right.
print(5 + 4 - 7 + 3) 
"""
5 + 4 = 9
9 - 7 = 2
2 + 3 = 5
Answer 5
"""