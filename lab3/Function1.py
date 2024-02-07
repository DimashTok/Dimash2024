
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#Ex1        Create a function to convert grams to ounces.

class q:
    def ounces(self, grams):
        result = grams * 28.3495231
        return result
my_instance = q()
gram_value = float(input())
ounces_result = my_instance.ounces(gram_value)
print(ounces_result)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#Ex2        Fahrenheit -> centigrade
class qw:
    def centigrade(self, F):
        C = (5/9)*(F-32)
        return C
my_instance = qw()
Farengate = float(input())
Celsi = my_instance.centigrade(Farengate)
print(Celsi)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#Ex3       KFC and bunny
class qwe:
    def headlegs(self, H, L):
        CH=(4*H-L)//2
        BU=(L-2*H)//2
        return CH, BU
my_instance = qwe()
HEAD = int(input())
LEG = int(input())
result = my_instance.headlegs(HEAD, LEG)
print(result)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#Ex4        prime
def isprime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
        return True
def filter_prime(numbers):
    return [num for num in numbers if isprime(num)]    
intnumbers=input()
numblist=list(map(int , intnumbers.split()))
result=filter_prime(numblist)
print(result)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#Ex 5 permutations
def permutations(string):
    if len(string) <= 1:
        return [string]
    
    perms = []
    for i in range(len(string)):
        current_char = string[i]
        remaining_chars = string[:i] + string[i+1:]
        for perm in permutations(remaining_chars):
            perms.append(current_char + perm)
    
    return perms

def print_permutations():
    user_input = input("Введите строку: ")
    perms = permutations(user_input)
    for perm in perms:
        print(perm)

print_permutations()

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#Ex6 reverse
def reverse_words(sentence):
    words = sentence.split()  
    reversed_sentence = ' '.join(reversed(words)) 
    return reversed_sentence
user_input = input()
reversed_sentence = reverse_words(user_input)
print(reversed_sentence)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#Ex7 3->3 TRUE
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
user_input = input()
nums = [int(x) for x in user_input.split()] 
result = has_33(nums)
print( result)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#Ex8 007->TRUE
def slovo_007(spisok):
    for i, num in enumerate(spisok):
        if num == 7 and spisok[:i].count(0) >= 2:
            return True
    return False

lists = list(map(int, input().split()))
result = slovo_007(lists)
print(result)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#Ex9        volume of a sphere
def volume(r):
    v=4/3*(r**3)*3.14
    return v
radius=int(input())
result=volume(radius)
print(result)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#Ex10 Uniqe
def unique_elements():
    user_input = input()
    lst = user_input.split()
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    
    return unique_list
result = unique_elements()
print(result)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#Ex11 palindrome
def polindrome(word):
    if word == word[::-1]:
        print('True')
    else:
        print('False')
slovo = input()
polindrome(slovo)    

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#Ex12       histogram
def histogram(n):
    print('*'*n)
def gf(q):
    for x in q:
        histogram(x)
zlist=list(map(int, input().split()))
gf(zlist)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#Ex13       play the "Guess the number"
import random
ran=random.randint(1,20)
attempt=1
print('Hello! What is your name?')
name=input()
print(f"Well,{name} I am thinking of a number between 1 and 20.")
print('Take a guess.')
while True:
    n=int(input())
    if n<ran:
        print('Your guess is too low.')    
        print('Take a guess.')
        attempt +=1
    elif n>ran:
        print('Your guess is too high.')    
        print('Take a guess.')
        attempt +=1
    else:
        print(f"Good job,{name}! You guessed my number in {attempt} guesses!")
        break    
    
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''    



    

       

