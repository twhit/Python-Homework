import os
import fnmatch

start_path = input("Enter a start path: ")
filename = input("Enter a file name: ")
found = False
for dirpath, dirs, files in os.walk(start_path):
    for file in files:
        if fnmatch.fnmatch(file, filename):
            print(os.path.join(dirpath, file) + " found.")
            found = True
            break
if not found:
    print("File not found.")

