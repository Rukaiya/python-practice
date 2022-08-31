import os

path = "/home/rukaiya/Development/Python_Practice"
for root, dirs, files in os.walk(path):
    # print("{0} has {1} files".format(root, len(files)))
    print(root, dirs, files)