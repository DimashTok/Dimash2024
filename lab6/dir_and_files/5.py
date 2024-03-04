import os
vvod = input()
spisok = list(map(int , vvod.split()))
with open("Sans.txt","w") as file:
    file.write(" ".join(map(str, spisok)))