import json
from datetime import datetime

json_path = './data/gskaggs.json'

def load_json(path):
    with open(path) as json_file:
        data = json.load(json_file)

        for book in data:
            for card in book['cards']:
                card['date'] = datetime.strptime(card['date'], '%Y-%m-%d').date()

        return data


def save_json(data, path):
    with open(path, 'w') as json_file:
        json.dump(data, json_file, indent=4, default=str)


def multiline_input(prompt):
    print(prompt)
    res = []
    while True:
        s = input()
        if len(s) == 0:
            break
        res.append(s)
    return '\n'.join(res)