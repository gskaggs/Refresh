import json
from datetime import datetime

json_path = './data/data.json'


def load_data(path):
    with open(path) as json_file:
        data = json.load(json_file)
        user_data, book_data = data['user'], data['books']
        for book in book_data:
            for card in book['cards']:
                card['date'] = datetime.strptime(card['date'], '%Y-%m-%d').date()

        return (user_data, book_data)


def save_data(user_data, book_data, path):
    with open(path, 'w') as json_file:
        data = {'user': user_data, 'books': book_data}
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