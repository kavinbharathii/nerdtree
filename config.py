# configuration variables

# current version
version = "2.2.1"

# current devs
dev = ["[developer]   == Kavin Bharathi {cipherDOT}",
       "[github page] == github.com/cipherDOT"]

# github page for the project
web = "https://github.com/cipherDOT/nerdtree"

# helping commands
help_cmd = [
    "-v    : shows the current version of nerdtree",
    "-dev  : shows the developers of nerdtree",
    "-help : displays the commands necessary to work with nerdtree",
    "-ls   : list all directories without sub directories",
    "-web  : output the github repo for nerdtree project",
    "-loc  : output the full path to the argument (file_name) if present in the cwd or in the dirs in cwd"
    "-help : list all the usable commands when using nerdtree"
]

# usage commands
use_cmd = [
    "> nerdtree            : shows the file structure in the current working directory",
    "> nerdtree -ls        : shows the file structure in cwd without the sub directories",
    "> nerdtree [path]     : shows the file structure in the given working directory",
    "> nerdtree [path] -ls : shows the file structure in given without the sub directories",
]
