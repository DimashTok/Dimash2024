#Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.

def squers(start, end):
    for i in range(start, end):
        yield i**2
        start +=1
chislo1 = int(input())
chislo2 = int(input())
spisok = squers(chislo1, chislo2)        
print(list(spisok))
    
    