import os

folder = "G:\Game\File\download"
movieTypes = set(["avi", "mp4", "mkv", "rmvb", "wmv"])

for fpath, dirs, fs in os.walk(folder):
    for filename in fs:
        fullpath = os.path.join(fpath, filename)
        suffix = filename[-3:]
        if filename[0:1] != "." and len(filename) > 4 and suffix in movieTypes:
            newFileName = filename[:-4] + ".txt"
            newFullPath = fpath + "/" + newFileName;
            print("createFile: " + newFullPath)
            file = open(newFullPath, "wt");
            file.close();

