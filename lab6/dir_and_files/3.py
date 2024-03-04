import os
def check_path(path):
    if os.path.exists(path):
        print("Path exists.")
        dirname = os.path.dirname(path)
        filename = os.path.basename(path)
        print(f"Directory name part: {dirname}")
        print(f"File name part: {filename}")
    else:
        print("Path does not exist.")
path_to_check = input("Enter the path to check: ")
check_path(path_to_check)
