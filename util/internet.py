import requests

def download(config, cache=False):
    base = "https://popcon.debian.org"
    by = config["by"]
    field = "by_"+config["field"]

    URL = "/".join([base, field]) if by == "whole" else "/".join([base, by, field])
    r = requests.get(URL)

    if cache:
        open("popcon.txt", "w").write(r.text)

    return r.text


