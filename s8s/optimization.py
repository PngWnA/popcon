import os
import re

pattern = re.compile(r"""-O\S+""")


# equivalent to grep
def ogrep(data, keyword):
    for line in data:
        if line.startswith(keyword):
            res = pattern.findall(line)
            if res != []:
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
            return res
        elif flag := ogrep(raw, "CXXFLAGS"):
            res["Makefile"] = flag
            return res

    elif "config.status" in path[2]:
        print("[+] config.status in root directory")
        raw = open(prefix+"/config.status", "r").readlines()
        if flag := ogrep(raw, "S[\"CFLAGS\"]"):
            res["config.status"] = flag
            return res
        elif flag := ogrep(raw, "S[\"CXXFLAGS\"]"):
            res["config.status"] = flag
            return res

    elif "configure" in path[2]:
        print("[+] configure in root directory")
        raw = open(prefix+"/configure", "r").readlines()
        if flag := ogrep(raw, "CFLAGS"):
            res["configure"] = flag
            return res
        elif flag := ogrep(raw, "CXXFLAGS"):
            res["configure"] = flag
            return res
    
    elif "Makefile.am" in path[2]:
        print("[+] Makefile.am in root directory")
        raw = open(prefix+"/Makefile.am", "r").readlines()
        if flag := ogrep(raw, "CFLAGS"):
            res["Makefile.am"] = flag
            return res
        elif flag := ogrep(raw, "CXXFLAGS"):
            res["Makefile.am"] = flag
            return res
    
    elif "configure.ac" in path[2]:
        print("[+] configure.ac in root directory")
        raw = open(prefix+"/configure.ac", "r").readlines()
        if flag := ogrep(raw, "AC_PROG_CC"):
            res["configure.ac"] = flag
            return res
        elif flag := ogrep(raw, "AC_PROG_CXX"):
            res["configure.ac"] = flag
            return res
    
    if res is None:
        res["default":"-O0"]

    return res



# Return optimization level of main target package
def check_opt_level():
    lst = list(os.walk("./"))
    
    root = lst[1]

    ''' 
    Check from
    * Makefile -> config.status -> Configure -> Makefile.am -> Configure.ac
    '''
    
    res = guess_opt_level(root)
    return res

