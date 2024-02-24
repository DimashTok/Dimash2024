import re
def split_at_uppercase(Stroka):
    split_parts = re.findall('[A-Z][^A-Z]*', Stroka)
    return split_parts
Stroka = "HelloWorld"
result = split_at_uppercase(Stroka)
print(result)
