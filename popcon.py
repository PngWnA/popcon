import os

from config import load_config
from util.internet import download_popcon, get_source
from util.parser import parse_popcon
from s8s.optimization import check_opt_level

#config = load_config()
#popcon = download_popcon(config["statistics"])
#lst = parse_popcon(popcon, config["parser"])



os.chdir("./tmp")
check_opt_level()
exit()

target = "./tmp"
total = len(lst)
for package in lst:
    print(f"{package['rank']}/{total} : {package['name']}")
    os.mkdir(target)
    os.chdir(target)
    # get_source(package["name"])
    check_opt_level()
    # Do something
    os.chdir("../")
    os.rmdir(target)