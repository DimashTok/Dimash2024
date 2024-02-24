import re
text = "Sabnautica is the best game after Minecraft, in my opinion"
print(re.findall('[A-Z][a-z]+', text))