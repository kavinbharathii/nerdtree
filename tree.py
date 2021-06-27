
# --------------------------------------------imported libraries---------------------------------------------- #
import sys
import os
from config import version, dev, web, help

# --------------------------------getting the sys argument to provide the path-------------------------------- #

try:
    arg_1 = str(sys.argv[1])
except Exception:
    arg_1 = None

# ----------------------------recursive algorithm to output the directory structure---------------------------- #


def nerdtree(path=os.getcwd(), count=0):
    dirs = os.listdir(path)
    dirs.sort(key=lambda x: os.path.isdir(x))
    space = "    "
    for dir in dirs:
        dir_path = path + '/' + dir
        if os.path.isdir(dir_path):
            print(f"{count * space}=> {dir}")
            count += 1
            nerdtree(dir_path, count)
            count -= 1
        elif os.path.isfile(dir_path):
            print(f"{count * space}- {dir}")

# ------------------------------executing the nerdtree function to output the tree------------------------------ #


if arg_1 != None:
    if arg_1 == '-v':
        print(f"{version}")
    elif arg_1 == '-dev':
        print(f"{dev}")
    elif arg_1 == "-help":
        print(f"{help}")
    elif arg_1 == "-web":
        print(f"{web}")
    else:
        nerdtree(arg_1)
else:
    nerdtree()

# -------------------------------------------------------------------------------------------------------------- #
