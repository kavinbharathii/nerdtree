# configuration variables

# current version
version = "version 3.5.1"

# current devs
dev = ["[developer]   == Kavin Bharathi {kavinbharathii}",
        "[github repo] == https://github.com/kavinbharathii"]

# github page for the project
web = "https://github.com/kavinbharathii/nerdtree"

# helping commands
help_cmd = [
    "-v    : shows the current version of nerdtree",
    "-dev  : shows the developers of nerdtree",
    "-h    : displays the commands necessary to work with nerdtree",
    "-el   : list all directories with sub directories",
    "-web  : output the github repo for nerdtree project",
    "-loc  : output the full path to the argument (file_name) if present in the cwd or in the dirs in cwd",
    "-cp   : copy a file to new file if name is specified. Else it creates {original_name}_copy file."
]

# usage commands
use_cmd = [
    "> ntr            : shows the file structure in the current working directory",
    "> ntr -el        : shows the file structure in cwd with the sub directories",
    "> ntr [path]     : shows the file structure in the given working directory",
    "> ntr [path] -el : shows the file structure in given with the sub directories",
]

# logo
logo = [
    " ._   _  ._ _| _|_ ._ _   _  ", 
    " | | (/_ | (_|  |_ | (/_ (/_ "
]
