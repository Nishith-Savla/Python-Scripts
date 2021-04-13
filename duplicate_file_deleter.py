import os
import sys

file_list = []
if sys.argv:
    currdir = sys.argv[1]
else:
    currdir = input("Enter the directory path to check duplicates in: ")
for directories, folders, files in os.walk(currdir):
    if len(files) > 1:
        print(files)
