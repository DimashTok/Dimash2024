stroka = str(input())
reversed_stroka = ''.join(reversed(stroka))
length = len(stroka)
count = 0
for i in range(length):
    if stroka[i] == reversed_stroka[i]:
        count += 1
    else:
        count = 0
        break
if count == length:
    print(True)
else:
    print(False)    
