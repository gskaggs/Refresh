#! /usr/bin/python3

import json
import random
from datetime import date, timedelta, datetime


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


def generate_front(quote):
    quote = quote.split()
    N = len(quote)
    K = N//4

    for i in random.choices(range(N), k=K):
        quote[i] = ''.join(['_'] * len(quote[i]))

    return ' '.join(quote)


def get_front_back(card):
    if card['type'] == 'flash':
        return (card['front'], card['back'])
    
    quote = card['quote']
    return ('Quote: ' + generate_front(quote), quote)


def present_card(card):
    front, back = get_front_back(card)
    
    input(front)
    response = input(back + '\n')

    return response.lower().strip() != 'f'


def update_card(card, successful):
    level_to_days = {1: 1, 2: 3, 3: 7, 4: 14}
    level = card['level']
    if successful:
        card['date'] = date.today() + timedelta(days=level_to_days[level])
        card['level'] = min(card['level'] + 1, 4)
    else:
        card['level'] = 1


def practice(data):
    for book in data:
        cards = book['cards']
        while any([card['date'] <= date.today() for card in cards]):
            print(book['title'])

            for card in cards:
                if card['date'] <= date.today():
                    successful = present_card(card)
                    update_card(card, successful)
                    print('')


if __name__ == '__main__':
    json_path = './data/gskaggs.json'
    data = load_json(json_path)
    practice(data)
    save_json(data, json_path)
