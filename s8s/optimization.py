import os

from tomlkit import key

# equivalent to grep
def ogrep(data, keyword):
    for line in data:
        if line.startswith(keyword):
            print(line)
    return


# Simple heuristic to guess the opt level
def guess_opt_level(path):
    prefix = path[0]
    res = {}


    if "Makefile" in path[2]:
        print("[+] Makefile in root directory")
        raw = open(prefix+"/Makefile", "r").readlines()
        if ogrep(raw, "CFLAGS"):
            print("wow")
    if "config.status" in path[2]:
        print("[+] config.status in root directory")
    if "configure" in path[2]:
        print("[+] configure in root directory")
    if "Makefile.am" in path[2]:
        print("[+] Makefile.am in root directory")
    if "configure.ac" in path[2]:
        print("[+] configure.ac in root directory")
    return



# Return optimization level of main target package
def check_opt_level():
    lst = list(os.walk("./"))
    
    root = lst[1]

    ''' 
    Check from
    * Makefile -> config.status -> Configure -> Makefile.am -> Configure.ac
    '''
    
    res = guess_opt_level(root)
    return

