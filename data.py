import json
INST_USER = INST_PASS = ''
HASHTAGS = []

def init():
    global INST_USER, INST_PASS, HASHTAGS
    data = None
    with open('settings.json', 'r') as myfile:
        data = myfile.read()
    obj = json.loads(data)
    INST_USER = obj['instagram']['user']
    INST_PASS = obj['instagram']['pass'] 
    HASHTAGS = obj['config']['hashtags']
 
