import requests
import os

# Return popcon raw statistics
def download_popcon(config, cache=False):
    base = "https://popcon.debian.org"
    by = config["by"]
    field = "by_"+config["field"]

    URL = "/".join([base, field]) if by == "whole" else "/".join([base, by, field])
    r = requests.get(URL)

    if cache:
        open("popcon.txt", "w").write(r.text)

    return r.text

# Unpack source code to current directory
def get_source(package):
    os.system(f"sudo apt source -y {package}")
    return