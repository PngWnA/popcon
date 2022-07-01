import os

from config import load_config
from util.internet import download_popcon, get_source
from util.parser import parse_popcon
from s8s.optimization import check_opt_level

config = load_config()
popcon = download_popcon(config["statistics"])
lst = parse_popcon(popcon, config["parser"])

target = "./tmp"
total = len(lst)
res = open("./result.txt", "w")

for package in lst:
    print(f"{package['rank']}/{total} : {package['name']}")
    os.mkdir(target)
    os.chdir(target)
    get_source(package["name"])
    res.write(f"{package['rank']} : {package['name']} : ")
    res.write(str(check_opt_level()))
    res.write("\n")
    os.chdir("../")
    os.rmdir(target)