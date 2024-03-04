import os 
for i in range(1, 27):
    q = i + 64
    let = chr(q)
    os.mkdir(f"{let}.txt")