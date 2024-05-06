
# [ ] nerdtree          {""  command}
# [ ] branched nerdtree {"-el"  command}
# [ ] locate            {"-loc" command}

import os
import shutil 
from pathlib import Path

space = 4 * " "
FORBIDDEN_DIRS = ["node_modules", "__pycache__", "venv", "target", "webpack", "prisma"]

# ----------------------------recursive algorithm to output the directory structure---------------------------- #

# the directory structure is given as:
#       => dirs
#           => sub_dir
#               -- sub_file.ext
#           -- file.ext
#           -- file.ext
#       -- file.ext
#       -- file.ext


def branched_nerdtree(path=os.getcwd(), count=0):

    # list of all the files and folders
    total_dirs = os.listdir(path)

    # filtering only the directories
    dirs = [x for x in total_dirs if os.path.isdir(path + '/' + x)]

    # filtering only the files
    fils = [x for x in total_dirs if os.path.isfile(path + '/' + x)]

    # directory output
    for dir in dirs:

        # find the directory path
        dir_path = path + '/' + dir
        print(f"{count * space}=> {dir}")

        # if the name of the directory is in FORBIDDEN_DIRS 
        # (which usually holds unusable info) omit the dirs.
        # or of the direcotry name starts with an ".", skip it
        if dir in FORBIDDEN_DIRS or dir[0] == ".":
            continue

        # recursive call to go into sub directories
        count += 1
        branched_nerdtree(dir_path, count)
        count -= 1

    # file output
    for fil in fils:
        print(f"{count * space}-- {fil}")

# ---------------------------nerdtree hidden(-la) structure layout algorithm(non recursive)-------------------------- #

# the directory structure is given as:
#       => dirs
#       -- file.ext
#       -- file.ext


def nerdtree(path=os.getcwd(), space = ''):
    # list of all the files and folders
    total_dirs = os.listdir(path)

    # filtering only the directories
    dirs = [x for x in total_dirs if os.path.isdir(path + '/' + x)]

    # filtering only the files
    fils = [x for x in total_dirs if os.path.isfile(path + '/' + x)]

    # directory and file output
    for dir in dirs:
        print(f"{space}=> {dir}")

    for fil in fils:
        print(f"{space}-- {fil}")

# ------------------------------------------------------------------------------------------------------------------ #

# the function:
#       [ ] full/path/to/file.name


def locate(path_name, path=os.getcwd()):

    try:
        total_dirs = os.listdir(path)
        dirs = [x for x in total_dirs if os.path.isdir(path + '/' + x)]
        fils = [x for x in total_dirs if os.path.isfile(path + '/' + x)]

        # list to store all the file names found matching
        results = []
        for fil in fils:
            if path_name in fil:
                # rpath is to present the dile name cleaner without mismatching '/' and '\'
                rpath = fr"{path}".replace("\\", "/")
                results.append(f"[ ] {rpath}/{fil}")

        for dir in dirs:
            if path_name in dir:
                # rpath is to present the dile name cleaner without mismatching '/' and '\'
                rpath = fr"{path}".replace("\\", "/")
                results.append(f"[ ] {rpath}/{dir}")

        # if no matching file names are found we go on to the next sub_directory
        if len(results) == 0:
            for dir in dirs:
                dir_path = path + '/' + dir
                locate(path_name, dir_path)

        elif len(results) >= 1:
            for r in results:
                print(f"{r}\n")

    except PermissionError:
        pass
    

# ------------------------------------------------------------------------------------------------------------------ #

def filecopy(origin, target = None, path=os.getcwd()):
    if target:
        if origin in os.listdir(path):
            origin = f"{path}/" + origin.split('/')[-1]
            target = f"{path}/" + target.split('/')[-1]
            shutil.copyfile(origin, target)
            print(f"[file {origin} copied to {target}]")
        else:
            try:
                shutil.copyfile(origin, target)
            except:
                print("[Error in 'target but not origin in path']")
    else:
        try:
            copyfilelist = origin.split(".")
            newfilename = "".join(copyfilelist[:-1]) + '_copy.' + copyfilelist[-1]
            copypath = path + '/' + newfilename
            shutil.copyfile(origin, copypath)
        except:
            pass
# ------------------------------------------------------------------------------------------------------------------ #
