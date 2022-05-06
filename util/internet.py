import requests
import os

def download_popcon(config, cache=False):
    base = "https://popcon.debian.org"
    by = config["by"]
    field = "by_"+config["field"]

    URL = "/".join([base, field]) if by == "whole" else "/".join([base, by, field])
    r = requests.get(URL)

    if cache:
        open("popcon.txt", "w").write(r.text)

    return r.text


def get_source(package, path):
    if not os.path.exists(path):
        os.mkdir(path)
    
    pwd = os.getcwd()
    os.chdir(path)
    os.system(f"sudo apt source -y {package}")
    os.chdir(pwd)