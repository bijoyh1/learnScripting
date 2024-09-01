import os

print("current Directory: " + os.getcwd())
dirList = os.listdir("/")
print("List directories in Home Folder: ")
print(dirList)
print("os.name: " + os.name)