
# version 2.2.1:
#       [ ] added error handling to invalid arguments

# todo:
#       [ ] improve usablity of code

# --------------------------------------------imported libraries---------------------------------------------- #
import sys
import os
from algos import locate, nerdtree, hidden_nerdtree, error_message
from config import version, dev, web, help_cmd, use_cmd

space = "    "

# getting a list of all the usable commands for nerdtree
commands = [x.split(':')[0].strip() for x in help_cmd]

# --------------------------------getting the sys argument to provide the path-------------------------------- #

try:
    # figuring whether a first argument is given
    arg_1 = str(sys.argv[1])

    try:
        # figuring whether a second argument is given
        arg_2 = str(sys.argv[2])
    except Exception:
        arg_2 = None

except Exception:
    arg_1 = None


# ------------------------------executing the nerdtree function to output the tree------------------------------ #


if arg_1 != None:

    if arg_2 != None:

        # if "-ls" is added with first argv, then we should take the path(argv[1]) and the hide{-ls} cmd(argv[2])
        if arg_2 == '-ls':
            # hidden nerdtree with the given path
            hidden_nerdtree(arg_1)

        if arg_1 == '-loc':
            locate(arg_2)

        else:
            error_message(arg_2)
    else:
        if arg_1 in commands:
            # -v - version
            if arg_1 == '-v':
                print(f"{version}")

            # "-dev" - name of developers
            elif arg_1 == '-dev':
                for i in dev:
                    print(space + i)

            # "-help" - help section
            elif arg_1 == "-help":
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

            # hidden nerdtree with the cwd path
            elif arg_1 == "-ls":
                hidden_nerdtree()

            # -loc without filename [ error handling ]
            elif arg_1 == "-loc":
                print("[ERROR] : give a name or a part of a name of a file to locate")

        elif arg_1[0] == '-':
            error_message(arg_1)
            # nerdtree runs at given location
        else:
            nerdtree(arg_1)
else:
    nerdtree()


# -------------------------------------------------------------------------------------------------------------- #
