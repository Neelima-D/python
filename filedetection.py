import os
path="C:\\Users\\Dasari\\Downloads\\neeli.txt"
if os.path.exists(path):
    print("that exists")
    if os.path.isfile(path):
        print("that is a file")
    elif os.path.isdir(path):
        print("that is a directory")
else:
    print("that doesn't exists")