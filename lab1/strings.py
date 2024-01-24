# 'Hellow' одно и тоже "Hellow"
print("Hello")
print('Hello')


#Присвоить строку переменной
a = "Hello"
print(a)


#можно присвоить переменной многострочную строку, используя три кавычки:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


#строки это массивы
a = "Hello, World!"
print(a[1]) #для получения первого элемента(как и в с++ тут все начинается с 0)


for x in "banana":
  print(x) 
"""
тот же цикл for
вывод
b
a
n
a
n
a
"""


#Длина строки
a = "Hello, World!"
print(len(a))


#Чтобы проверить, присутствует ли в строке определенная фраза или символ,
# мы можем использовать ключевое слово in.
txt = "The best things in life are free!"
print("free" in txt)


#с условием
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


#Чтобы проверить, НЕ присутствует ли определенная фраза или символ в строке,
# мы можем использовать ключевое слово not in.
txt = "The best things in life are free!"
print("expensive" not in txt)


#с условием
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

''''''

#можно нарезать, тоесть вырезать кусок строки в определенном диапозоне
b = "Hello, World!"
print(b[2:5])

#Разрез с самого начала
b = "Hello, World!"
print(b[:5])

#Разрезать до конца
b = "Hello, World!"
print(b[2:])

#Отрицательная индексация, тоесть в обратном порядке
b = "Hello, World!"
print(b[-5:-2])

''''''

#upper() возвращает строку в верхнем регистре:
a = "Hello, World!"
print(a.upper())

#lower() возвращает строку в нижнем регистре:
a = "Hello, World!"
print(a.lower())

#strip() удаляет любые пробелы в начале или конце:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#replace() заменяет строку другой строкой:
a = "Hello, World!"
print(a.replace("H", "J"))

#split()разбивает строку на подстроки, если находит экземпляры разделителя:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

''''''

#Объединить переменную aс переменной bв переменную c:
a = "Hello"
b = "World"
c = a + b
print(c)

#добавить пробел между ними, добавьте " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)


''''''

"""
мы так не можем
age = 36
txt = "My name is John, I am " + age
print(txt)
"""
#но мы можем юзать format()
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
#мы заменяем {} на age

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
#{} эти штуки будут заменяться в порядки очереди тоесть 
# с перва quantity потом itemno потом price

#Вы можете использовать индексные номера {0}, чтобы убедиться, что аргументы помещены в правильные заполнители:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
#quantity индекс 0
# itemno индекс 1
#price индекс 2

''''''

#мы не можем написать так "PWGood started the "Pepeland 8" and hi is sick"
#тоесть не можем постпаить внутри ковечек еще одни ковычки
#что бы можно было так писать нужно юзать \"текст\"   "PWGood started the \"Pepeland 8\" and hi is sick"
txt = "We are the so-called \"Vikings\" from the north."
# И остальное 

txt = 'It\'s alright.'
print(txt) #  Single Quote вывод It's alright.

txt = "This will insert one \\ (backslash)."
print(txt) #	Backslash вывод This will insert one \ (backslash).

txt = "Hello\nWorld!"        #Hello
print(txt) #	New Line вывод World!

txt = "Hello\rWorld!"               #Hello
print(txt) #	Carriage Return вывод World!

txt = "Hello\tWorld!"
print(txt) #  Tab вывод Hello   World!

txt = "Hello \bWorld!"
print(txt) #В этом примере удаляеться один символ (	Backspace) вывод HelloWorld!

txt = "\110\145\154\154\157"
print(txt) #Обратная косая черта, за которой следуют три целых числа, дает восьмеричное значение:
        # 	Octal value  вывод Hello

txt = "\x48\x65\x6c\x6c\x6f"
print(txt) #Обратная косая черта, за которой следует 'x' и шестнадцатеричное число, представляют собой шестнадцатеричное значение:
           #Hex value вывод Hello

''''''
#capitalize() Преобразует первый символ в верхний регистр
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

#casefold() Преобразует строку в нижний регистр 
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

#center() Возвращает центрированную строку
txt = "banana"
x = txt.center(20)
print(x) #вывод       banana

#count() Возвращает количество раз, когда указанное значение встречается в строке
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

#encode() Возвращает закодированную версию строки
txt = "My name is Ståle"
x = txt.encode()
print(x)

#endswith() Возвращает true, если строка заканчивается указанным значением
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x) 

#expandtabs() Устанавливает размер табуляции строки
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)

#find() Ищет в строке указанное значение и возвращает позицию, где оно было найдено.
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

#format() Форматирует указанные значения в строке
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

#format_map() Форматирует указанные значения в строке

#index()Ищет в строке указанное значение и возвращает позицию, где оно было найдено.
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)   

#isalnum() Возвращает True, если все символы в строке являются буквенно-цифровыми.
txt = "Company12"
x = txt.isalnum()
print(x)

#isalpha() Возвращает значение True, если все символы строки находятся в алфавите.
txt = "CompanyX"
x = txt.isalpha()
print(x)

#isascii() Возвращает значение True, если все символы в строке являются символами ascii.
txt = "Company123"
x = txt.isascii()
print(x)

#isdecimal() Возвращает True, если все символы в строке являются десятичными.
txt = "1234"
x = txt.isdecimal()
print(x)

#isdigit() Возвращает True, если все символы в строке — цифры.
txt = "50800"
x = txt.isdigit()
print(x)

#isidentifier() Возвращает True, если строка является идентификатором
txt = "Demo"
x = txt.isidentifier()
print(x)

#islower() Возвращает значение True, если все символы в строке написаны строчными буквами.
txt = "hello world!"
x = txt.islower()
print(x)

#isnumeric() Возвращает True, если все символы в строке числовые.
txt = "565543"
x = txt.isnumeric()
print(x)

#isprintable() Возвращает значение True, если все символы строки можно распечатать.
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)

#isspace() Возвращает True, если все символы в строке являются пробелами.
txt = "   "
x = txt.isspace()
print(x)

#istitle() Возвращает True, если строка соответствует правилам заголовка
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)

#isupper() Возвращает значение True, если все символы в строке имеют верхний регистр.
txt = "THIS IS NOW!"
x = txt.isupper()
print(x)

#join() Присоединяет элементы итерации к концу строки
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

#ljust() Возвращает версию строки, выровненную по левому краю.
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")

#lower() Преобразует строку в нижний регистр
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)

#lstrip() Возвращает версию строки с обрезкой слева
txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")

#maketrans() Возвращает таблицу перевода, которая будет использоваться в переводах.
txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))

#partition() Возвращает кортеж, в котором строка разделена на три части
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)

#replace() Возвращает строку, в которой указанное значение заменяется указанным значением.
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

#rfind() Ищет в строке указанное значение и возвращает последнюю позицию, где оно было найдено.
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)

#rindex() Ищет в строке указанное значение и возвращает последнюю позицию, где оно было найдено.
txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)

#rjust() Возвращает выровненную по правому краю версию строки
txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")

#rpartition() Возвращает кортеж, в котором строка разделена на три части
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)

#rsplit() Разбивает строку по указанному разделителю и возвращает список
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)

#rstrip() Возвращает правильную обрезанную версию строки
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")

#split() Разбивает строку по указанному разделителю и возвращает список
txt = "welcome to the jungle"
x = txt.split()
print(x)

#splitlines() Разбивает строку на разрывах строк и возвращает список
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)

#startswith() Возвращает true, если строка начинается с указанного значения
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)

#strip() Возвращает обрезанную версию строки
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")

#swapcase() Меняет регистры, нижний регистр становится прописным и наоборот.
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)

#title() Преобразует первый символ каждого слова в верхний регистр.
txt = "Welcome to my world"
x = txt.title()
print(x)

#translate() Возвращает переведенную строку
#используйте словарь с кодами ascii, чтобы заменить 83 (S) на 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))

#upper() Преобразует строку в верхний регистр
txt = "Hello my friends"
x = txt.upper()
print(x)

#zfill() Заполняет строку указанным количеством значений 0 в начале
txt = "50"
x = txt.zfill(10)
print(x)

''''''