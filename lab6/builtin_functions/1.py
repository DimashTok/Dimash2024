spisok = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(map(lambda x : x * 10, spisok)))
count = 1
for i in spisok:
    count = count * i
print(count)