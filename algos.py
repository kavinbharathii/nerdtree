
# [ ] nerdtree
# [ ] hidden nerdtree {"-ls" command}
# [ ] locate          {"-loc" command}

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

    # list of all the files and folders
    total_dirs = os.listdir(path)

    # filtering only the directories
    dirs = [x for x in total_dirs if os.path.isdir(path + '/' + x)]

    # filtering only the files
    fils = [x for x in total_dirs if os.path.isfile(path + '/' + x)]

    # directory output
    for dir in dirs:
        dir_path = path + '/' + dir
        print(f"{count * space}=> {dir}")

        # recursive call to go into sub directories
        count += 1
        nerdtree(dir_path, count)
        count -= 1

    # file output
    for fil in fils:
        print(f"{count * space}-- {fil}")

# ---------------------------nerdtree hidden(-la) structure layout algorithm(non recursive)-------------------------- #

# the directory structure is given as:
#       => dirs
#       -- file.ext
#       -- file.ext


def hidden_nerdtree(path=os.getcwd()):
    # list of all the files and folders
    total_dirs = os.listdir(path)

    # filtering only the directories
    dirs = [x for x in total_dirs if os.path.isdir(path + '/' + x)]

    # filtering only the files
    fils = [x for x in total_dirs if os.path.isfile(path + '/' + x)]

    # directory and file output
    for dir in dirs:
        print(f"=> {dir}")

    for fil in fils:
        print(f"-- {fil}")

# ------------------------------------------------------------------------------------------------------------------ #

# the function:
#       [ ] full/path/to/file.name


def locate(file, path=os.getcwd()):

    total_dirs = os.listdir(path)
    dirs = [x for x in total_dirs if os.path.isdir(path + '/' + x)]
    fils = [x for x in total_dirs if os.path.isfile(path + '/' + x)]

    # list to store all the file names found matching
    results = []
    for fil in fils:
        if file in fil:
            # rpath is to present the dile name cleaner without mismatching '/' and '\'
            rpath = fr"{path}".replace("\\", "/")
            results.append(f"[ ] {rpath}/{fil}")

    # if no matching file names are found we go on to the next sub_directory
    if len(results) == 0:
        for dir in dirs:
            dir_path = path + '/' + dir
            locate(file, dir_path)

    elif len(results) >= 1:
        for r in results:
            print(f"{r}\n")


# ------------------------------------------------------------------------------------------------------------------ #

def error_message(invalid_arg):
    print(f"'{invalid_arg}' : Invalid Command or Request")
    print("Try using 'nerdtree -help'")

# ------------------------------------------------------------------------------------------------------------------ #
