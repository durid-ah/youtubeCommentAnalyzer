import json


def get_data():
    json_file = open('./../projectSecrets.json')
    data = json.load(json_file)
    json_file.close()
    return data


Secrets = get_data()
