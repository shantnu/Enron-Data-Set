import os

rootdir = "C:\\Users\\Shantnu\\Desktop\\Data Sources\\maildir\\"

for directory, subdirectory, filenames in  os.walk(rootdir):
    print(directory, subdirectory, len(filenames))