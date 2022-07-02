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

if os.path.exists("./result.txt"):
    res = open("./result.txt", "a")
    last = open("./result.txt", "r").readlines()
    print(last[-2:])
    if last[-1] != "\n":
        start = int(last[-1].split(":")[0])
    else:
        start = int(last[-2].split(":")[0])
else:
    res = open("./result.txt", "w")
    start = 0

for package in lst[start:]:
    print(f"{package['rank']}/{total} : {package['name']}")
    os.mkdir(target)
    os.chdir(target)
    get_source(package["name"])
    opt = str(check_opt_level())
    res.write(f"{package['rank']} : {package['name']} : ")
    res.write(opt)
    res.write("\n")
    os.chdir("../")
    os.system(f"sudo rm -rf {target}")
