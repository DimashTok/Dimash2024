import os
count = 0
with open("Sans.txt", "r") as file:
    for line in file:
        count += 1
print(count)    