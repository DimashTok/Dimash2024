import os
def display_directory_contents(path):
    print("Catalogs:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print("-", item)

    print("\nFiles:")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print("-", item)

    print("\nNested directories and files:")
    for root, dirs, files in os.walk(path):
        print(f"Catalog: {root}")
        for directory in dirs:
            print(f" -Subdirectory: {os.path.join(root, directory)}")
        for file in files:
            print(f" -File: {os.path.join(root, file)}")
path_to_display = input("Enter directory path: ")

if os.path.exists(path_to_display):
    display_directory_contents(path_to_display)
else:
    print("The specified path does not exist.")
