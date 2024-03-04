import re
stroka = "My name is Dimash and I played Undertale with Deltarune"
upper_case_letters_sample = re.findall(r'[A-Z]',stroka)
lower_case_letters_sample = re.findall(r'[a-z]',stroka)
upper_case_letters_sample_count = len(upper_case_letters_sample)
lower_case_letters_sample_count = len(lower_case_letters_sample)
print(f"upper case letters count in stroka is: {upper_case_letters_sample_count}")
print(f"lower case letters count in stroka is: {lower_case_letters_sample_count}")

