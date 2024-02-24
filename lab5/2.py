import re
text = "asddcvwqcfvxabbacabbbbadcqfwefabb"
print(re.findall('ab{2,3}', text))