from functools import cache
from init import init
from util.internet import download
from util.parser import parse

config = init()
popcon_txt = download(config["statistics"])
popcon_lst = parse(popcon_txt, config["parser"])