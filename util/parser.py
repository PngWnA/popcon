import re

# (?P<maintainer>\(.+\))
pattern = re.compile( \
    r"^(?P<rank>\d+)\s+" + \
    r"(?P<name>\S+)\s+" + \
    r"(?P<inst>\d+)\s+" + \
    r"(?P<vote>\d+)\s+" + \
    r"(?P<old>\d+)\s+" + \
    r"(?P<recent>\d+)\s+" + \
    r"(?P<nofiles>\d+)\s+" + \
    r"\((?P<maintainer>.*)\)")

def parse(txt, config, cache=False):
    if cache:
        txt = open("cache/popcon.txt", "r").read()

    lines = txt.split("\n")
    rows = []

    for line in lines:
        if line.startswith("#"):
            continue
        else:
            match = pattern.match(line)
            rows.append(match.groupdict())
            if line.startswith(str(config["top"])):
                return rows
