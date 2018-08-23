import os, glob, shutil

BAK_DIR = "/Users/tony/MyProject/python/bak/"
"c:\\n\n"

os.chdir("/Users/tony/MyProject/python/day4/")

fileList = glob.glob("*.py")

if not os.path.exists(BAK_DIR):
  os.mkdir(BAK_DIR)

for file in fileList:
  shutil.copy(file, BAK_DIR)


shutil.make_archive("bak", "zip", BAK_DIR)

shutil.rmtree(BAK_DIR)