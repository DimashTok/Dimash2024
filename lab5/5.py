import re
text = "asb vcdsba sdyvai ababdb dbffhw ahudhb aaydb fyab"
words = text.split()
patern = r'^a.+b$'
for word in words:
    if re.findall(patern, word):
        print(word)
