import os
import re

pattern = re.compile(r"""-O\S+""")


# equivalent to grep
def ogrep(data, keyword):
    for line in data:
        if (not line.strip().startswith("#")) and (keyword in line):
            res = pattern.findall(line)
            if res != []:
                res = res[0].replace("\"", "")
                print(res)
                return res
    return None


# Simple heuristic to guess the opt level
def guess_opt_level(path):
    prefix = path[0]
    res = {}

    if "Makefile" in path[2]:
        print("[+] Makefile: ", end="")
        raw = open(prefix+"/Makefile", "r").readlines()
        if flag := ogrep(raw, "CFLAGS"):
            res["Makefile"] = flag
            return res
        elif flag := ogrep(raw, "CXXFLAGS"):
            res["Makefile"] = flag
            return res
        elif ogrep(raw, "CC"): 
            res["Makefile"] = "-O0" # default
            return res
        elif ogrep(raw, "CXX"):
            res["Makefile"] = "-O0" # default
            return res
        print()

    if "config.status" in path[2]:
        print("[+] config.status: ", end="")
        raw = open(prefix+"/config.status", "r").readlines()
        if flag := ogrep(raw, "S[\"CFLAGS\"]"):
            res["config.status"] = flag
            return res
        elif flag := ogrep(raw, "S[\"CXXFLAGS\"]"):
            res["config.status"] = flag
            return res
        print()

    if "configure" in path[2]:
        print("[+] configure: ", end="")
        raw = open(prefix+"/configure", "r").readlines()
        if flag := ogrep(raw, "CFLAGS"):
            res["configure"] = flag
            return res
        elif flag := ogrep(raw, "CXXFLAGS"):
            res["configure"] = flag
            return res
        else:
            res["configure"] = "-O2" # default
            return res
        print()

    if "Configure" in path[2]:
        print("[+] configure: ", end="")
        raw = open(prefix+"/Configure", "r").readlines()
        if flag := ogrep(raw, "CFLAGS"):
            res["configure"] = flag
            return res
        elif flag := ogrep(raw, "CXXFLAGS"):
            res["configure"] = flag
            return res
        else:
            res["configure"] = "-O2" # default
            return res
        print()

    if "Makefile.am" in path[2]:
        print("[+] Makefile.am: ", end="")
        raw = open(prefix+"/Makefile.am", "r").readlines()
        if flag := ogrep(raw, "CFLAGS"):
            res["Makefile.am"] = flag
            return res
        elif flag := ogrep(raw, "CXXFLAGS"):
            res["Makefile.am"] = flag
            return res
        print()
    
    if "configure.ac" in path[2]:
        print("[+] configure.ac: ", end="")
        raw = open(prefix+"/configure.ac", "r").readlines()
        if flag := ogrep(raw, "AC_PROG_CC"):
            res["configure.ac"] = flag
            return res
        elif flag := ogrep(raw, "AC_PROG_CXX"):
            res["configure.ac"] = flag
            return res
        else:
            res["configure"] = "-O2" # default
            return res
        print()

    if "CMakeLists.txt" in path[2]:
        print ("[*] CMakeLists.txt: ", end="")
        raw = open(prefix+"/CMakeLists.txt").readlines()
        if flag := ogrep(raw, "CMAKE_C_FLAGS"):
            res["CMakeLists.txt"] = flag
            return res
        elif flag := ogrep(raw, "CMAKE_CXX_FLAGS"):
            res["CMakeLists.txt"] = flag
            return res
        else:
            res["CMakeLists.txt"] = "-O0"
            return res
        print()

    if res == {}:
        res["NA"] = "X"

    return res



# Return optimization level of main target package
def check_opt_level():
    lst = list(os.walk("./"))
    print("[ ] Checking root directory...")
    if len(lst) < 2:
        res = {}
        res["Error"] = "X"
        return res
    root = lst[1]

    ''' 
    Check from
    * Makefile -> config.status -> Configure -> Makefile.am -> Configure.ac
    '''
    res = guess_opt_level(root)
    if ("NA" in res) and ("src" in root[1]):
        print("[ ] Checking src directory...")
        for directory in lst:
            print(directory)
            if directory[0].endswith("src"):
                res = guess_opt_level(directory)
                return res
    else:
        return res


