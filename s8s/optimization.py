import os

# Return optimization level of main target package
def check_opt_level():
    lst = list(os.walk("./"))
    
    root = lst[1]
    prefix = root[0]

    ''' 
    Check from
    * Makefile -> config.status -> Configure -> Makefile.am -> Configure.ac
    '''
    
    res = {}
    
    if "Makefile" in root[2]:
        print("[+] Makefile in root directory")
        raw = open(prefix+"/Makefile", "r").read()
        print(raw)
    if "config.status" in root[2]:
        print("[+] config.status in root directory")
    if "configure" in root[2]:
        print("[+] configure in root directory")
    if "Makefile.am" in root[2]:
        print("[+] Makefile.am in root directory")
    if "configure.ac" in root[2]:
        print("[+] configure.ac in root directory")

    return