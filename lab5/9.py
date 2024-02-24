import re
def space(stroka):
    words = re.findall(r'[A-Z][^A-Z]*',stroka)
    modded_stroka = ' '.join(words)
    return modded_stroka
vvod_stroki = 'IAmTheBestMinecraftPlayer'
result = space(vvod_stroki)
print(result)
    