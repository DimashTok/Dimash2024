x = 5
y = "Marmork"
print(x)
print(y) #Можно присваивать значения

z=4
z="yo"
print(z) #можно заменять значения

c=str(5)
v=int(5)
b=float(5) #можно задать какой тип будет значение(число, строка, число с запетой)

print(type(x))
print(type(y)) #можно узнать тип значения 

x = "Kuplinov"
# is the same as
x = 'Kuplinov'

a = 4
A = "Sally"
#A is not a

"""
Имя переменной должно начинаться с буквы или символа подчеркивания.
Имя переменной не может начинаться с цифры
Имя переменной может содержать только буквенно-цифровые символы и символы подчеркивания (Az, 0–9 и _).
Имена переменных чувствительны к регистру (возраст, Возраст и ВОЗРАСТ — три разные переменные).
Имя переменной не может быть ни одним из ключевых слов Python .
"""
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Имена переменных, состоящие из нескольких слов
myVariableName = "John"
MyVariableName = "John"
my_variable_name = "John"

xx, yy, zz = "Orange", "Banana", "Cherry"
print(xx)
print(yy)
print(zz) #можно сразу в одной строке задать значения для разных  x y z-ов

xxx = yyy = zzz = "Orange"
print(xxx)
print(yyy)
print(zzz) #можно сразу всем задать одно и то же значение

fruits = ["apple", "banana", "cherry"]
cc, vv, bb = fruits
print(cc)
print(vv)
print(bb) #можно распоковать значения из набора

q = "Python is awesome"
print(q) #вывод Python is awesome

qq = "Python"
ww = "is"
ee = "awesome"
print(qq, ww, ee) #вывод Python is awesome
print(qq + ww + ee) #вывод Python is awesome

x = 5
y = 10
print(x + y) #вывод 15

#так нельзя
"""
x = 5
y = "John"
print(x + y)
"""

#так можно
x = 5
y = "John"
print(x, y) #вывод 5
