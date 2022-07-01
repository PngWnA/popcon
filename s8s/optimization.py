import os
import re

pattern = re.compile(r"""-O\S+""")


# equivalent to grep
def ogrep(data, keyword):
    for line in data:
        if line.startswith(keyword):
            res = pattern.findall(line)
            if res is not None:
                return res[0]
    return None


# Simple heuristic to guess the opt level
def guess_opt_level(path):
    prefix = path[0]
    res = {}


    if "Makefile" in path[2]:
        print("[+] Makefile in root directory")
        raw = open(prefix+"/Makefile", "r").readlines()
        if flag := ogrep(raw, "CFLAGS"):
            res["Makefile"] = flag
            print(res)
    elif "config.status" in path[2]:
        print("[+] config.status in root directory")
    elif "configure" in path[2]:
        print("[+] configure in root directory")
    elif "Makefile.am" in path[2]:
        print("[+] Makefile.am in root directory")
    elif "configure.ac" in path[2]:
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

