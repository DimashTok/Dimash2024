import os
with open("C:/Users/Dimash/Desktop/Dimash2024PP2/lab6/dir_and_files/Sans.txt", "r") as file1:
    Sans_copied = file1.read()
with open("C:/Users/Dimash/Desktop/Dimash2024PP2/lab6/dir_and_files/Papyrus's_brother.txt", "w") as file2:
    file2.write(Sans_copied)  
