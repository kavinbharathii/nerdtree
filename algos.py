
# [ ] nerdtree
# [ ] hidden nerdtree {"-ls" command}

import sys
import os

space = "    "

# ----------------------------recursive algorithm to output the directory structure---------------------------- #

# the directory structure is given as:
#       => dirs
#           => sub_dir
#               -- sub_file.ext
#           -- file.ext
#           -- file.ext
#       -- file.ext
#       -- file.ext


def nerdtree(path=os.getcwd(), count=0):
    total_dirs = os.listdir(path)
    dirs = [x for x in total_dirs if os.path.isdir(path + '/' + x)]
    fils = [x for x in total_dirs if os.path.isfile(path + '/' + x)]
    for dir in dirs:
        dir_path = path + '/' + dir
        print(f"{count * space}=> {dir}")
        count += 1
        nerdtree(dir_path, count)
        count -= 1
    for fil in fils:
        print(f"{count * space}-- {fil}")

# ---------------------------nerdtree hidden(-la) structure layout algorithm(non recursive-------------------------- #

# the directory structure is given as:
#       => dirs
#       -- file.ext
#       -- file.ext


def hidden_nerdtree(path=os.getcwd()):
    total_dirs = os.listdir(path)
    dirs = [x for x in total_dirs if os.path.isdir(path + '/' + x)]
    fils = [x for x in total_dirs if os.path.isfile(path + '/' + x)]
    for dir in dirs:
        print(f"=> {dir}")
    for fil in fils:
        print(f"-- {fil}")

# ------------------------------------------------------------------------------------------------------------------ #
