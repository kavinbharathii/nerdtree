
# version 2.1.0:
#       [ ] nerdtree => with cleaner seperation
#       [ ] added hidden tree functionality
#       [ ] added new command ["-ls" => hidden tree]
#       [ ] cleaner code structure
#       [ ] added help functionality

# --------------------------------------------imported libraries---------------------------------------------- #
import sys
import os
from algos import nerdtree, hidden_nerdtree
from config import version, dev, web, help_cmd, use_cmd

space = "    "

# --------------------------------getting the sys argument to provide the path-------------------------------- #

try:
    arg_1 = str(sys.argv[1])

    try:
        arg_2 = str(sys.argv[2])
    except Exception:
        arg_2 = None

except Exception:
    arg_1 = None


# ------------------------------executing the nerdtree function to output the tree------------------------------ #


if arg_1 != None:

    if arg_2 != None:

        # if "-la" is added with first argv, then we should take the path(argv[1]) and the hidden cmd(argv[2])
        if arg_2 == '-ls':
            # hidden nerdtree with the given path
            hidden_nerdtree(arg_1)
    else:
        # -v - version
        if arg_1 == '-v':
            print(f"{version}")

        # "-dev" - name of developers
        elif arg_1 == '-dev':
            print(f"{dev}")

        # "-h" / "--help" - help menu
        elif arg_1 == "-h" or arg_1 == "--help":
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

        # nerdtree runs at given location
        else:
            nerdtree(arg_1)
else:
    nerdtree()


# -------------------------------------------------------------------------------------------------------------- #
