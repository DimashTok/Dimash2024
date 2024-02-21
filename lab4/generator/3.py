#Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.

def numbers(start, end):
    while start < end:
        if start%4 == 0:
            yield start
        elif start%3== 0:
            yield start
        start +=1
chislo = int(input())
spisok = numbers(0, chislo)        
print(list(spisok))
    
    