#Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.

def even_numbers(start, end):
    while start < end:
        if start%2 == 0:
            yield start
        start +=1
chislo = int(input())
spisok = even_numbers(0, chislo)        
print(list(spisok))
    
    