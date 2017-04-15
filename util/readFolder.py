import os

folder = "G:\Game\File\Ring\Y一"

paths = os.listdir(folder)
for path in paths:
    if not (path.lower().endswith("jpg")):
        print(path[0:-4])
