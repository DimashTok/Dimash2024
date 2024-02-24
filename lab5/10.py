import re
def camel_to_snake(stroka):
    modded_stroka = re.findall(r'[A-Z][^A-Z]*',stroka)
    modded_stroka_2 = '_'.join(modded_stroka)
    if modded_stroka_2.startswith('_'):
        modded_stroka_2 = modded_stroka_2[:1]
    return modded_stroka_2.lower()
slova = 'IaVerbludIIaNeDovolenEtim'
result = camel_to_snake(slova)
print(result)
