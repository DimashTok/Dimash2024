import re
text = "This is my text,What are you doing here?.BYEEE :)"
texts = re.sub(r'[ ,.]', ':', text)
print(texts)
