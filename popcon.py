from functools import cache
from init import init
from util.internet import download_popcon, get_source
from util.parser import parse_popcon

config = init()
popcon = download_popcon(config["statistics"])
lst = parse_popcon(popcon, config["parser"], cache=True)

for package in lst:
    get_source(package["name"], f"tmp/{package['name']}")