import os
def check_path_access(path):
    if os.path.exists(path):
        print(f"The path {path} exists.")
        if os.access(path, os.R_OK):
            print("Read permission is granted.")
        else:
            print("Read permission is denied.")
        if os.access(path, os.W_OK):
            print("Write permission is granted.")
        else:
            print("Write permission is denied.")
        if os.access(path, os.X_OK):
            print("Execute permission is granted.")
        else:
            print("Execute permission is denied.")
    else:
        print(f"The path {path} does not exist.")
path_to_check = input("Enter the path to check access: ")
check_path_access(path_to_check)
