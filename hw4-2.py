import os
import fnmatch

dir_path = input("Enter the file path: ")
filename = input("Enter the file name: ")

full_path = os.path.join(dir_path, filename)
if not os.path.isfile(full_path):
    print("File not found.")
else:
    f = open(full_path)
    contents = f.read()
    f.close()
    if (contents.find("password=") > 0):
        print("Plaintext password string found.")
    else:
        print("No plaintext password string found.")
