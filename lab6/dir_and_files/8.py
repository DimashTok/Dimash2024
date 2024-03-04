import os
def delete_file(file_path):
    if os.path.exists(file_path):
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"File {file_path} successfully deleted.")
        else:
            print(f"{file_path} is a directory, not a file.")
    else:
        print(f"File {file_path} does not exist.")
file_to_delete = input("Enter the path to the file for deletion: ")
delete_file(file_to_delete)
