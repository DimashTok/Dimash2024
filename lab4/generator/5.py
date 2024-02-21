#Implement a generator that returns all numbers from (n) down to 0.

def numbers(start, end):
    while start <= end:
        yield end
        end -=1
chislo = int(input())
spisok = numbers(0, chislo)        
print(list(spisok))