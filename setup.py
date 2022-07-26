
# version 3.6.0:
#       [ ] added 'cp' for copy pasting files from the terminal

# todo:
#       [ ] make a commands file to organize the code

# --------------------------------------------imported libraries---------------------------------------------- #
from ast import arg
import sys
from algos import locate, nerdtree, branched_nerdtree, filecopy
from config import version, dev, web, help_cmd, use_cmd, logo

space = 4 * " "

# --------------------------------getting the sys argument to provide the path-------------------------------- #

try:
    arg_1 = str(sys.argv[1])

    try:
        arg_2 = str(sys.argv[2])

        try:
            arg_3 = str(sys.argv[3])

        except Exception:
            arg_3 = None

    except Exception:
        arg_2 = None

except Exception:
    arg_1 = None


# ------------------------------executing the nerdtree function to output the tree------------------------------ #


if arg_1:
    if arg_2:

        # if "-la" is added with first argv, then we should take the path(argv[1]) and the branch{-el} cmd(argv[2])
        if arg_2 == '-el':
            # branched nerdtree with the given path
            branched_nerdtree(arg_1)

        if arg_1 == '-loc':
            locate(arg_2)

        if arg_1 == 'cp':
            if arg_3:
                filecopy(arg_2, arg_3)
            else:
                filecopy(arg_2)
    else:
        # -v - version
        if arg_1 == '-v':
            print(f"{version}")

        # "-dev" - name of developers
        elif arg_1 == '-dev':
            for i in dev:
                print(space + i)

        # "-h" / "--help" - help section
        elif arg_1 == "-h" or arg_1 == "--help":
            for logo_line in logo:
                print(logo_line)

            print()
            print("COMMANDS")
            for h in help_cmd:
                print(space + h)
            print("\n")
            print("USAGE")
            for u in use_cmd:
                print(space + u)

        # "-web" - shows the github page
        elif arg_1 == "-web":
            print(f"{web}")

        # branched nerdtree with the cwd path
        elif arg_1 == "-el":
            branched_nerdtree()

        # -loc without filename error handling
        elif arg_1 == "-loc":
            print("[ERROR] : give a name or a part of a name of a file to locate")

        elif arg_1 == "cp":
            print("Give a valid file name")

        # nerdtree runs at given location
        else:
            branched_nerdtree(arg_1)
else:
    nerdtree()

# -------------------------------------------------------------------------------------------------------------- #
