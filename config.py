import json

def load_config():
    return json.loads(open('config.json').read()) 

