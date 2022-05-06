import json

def init():
    return json.loads(open('config.json').read()) 

