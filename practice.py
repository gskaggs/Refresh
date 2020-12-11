#! /usr/bin/python3

import random
from datetime import date, timedelta
from utils import load_json, save_json, json_path

def generate_front(quote):
    quote = quote.split()
    N = len(quote)
    K = N//4

    for i in random.choices(range(N), k=K):
        quote[i] = ''.join(['_'] * len(quote[i]))

    return ' '.join(quote)


def get_front_back(card):
    card_type = card['type']
    if card_type == 'flash':
        return (card['front'], card['back'])

    if card_type == 'quote':
        quote = card['quote']
        return ('Quote: ' + generate_front(quote), quote)

    if card_type == 'note':
        note = card['note']
        return ('Note: ' + generate_front(note), note)


def present_card(card):
    front, back = get_front_back(card)
    
    input(front)
    response = input(back + '\n')

    return response.lower().strip() != 'f'


def update_card(card, successful):
    level_to_days = {1: 1, 2: 3, 3: 7, 4: 14, 5: 21}
    level = card['level']
    if successful:
        card['date'] = date.today() + timedelta(days=level_to_days[level])
        card['level'] = min(card['level'] + 1, 5)
    else:
        card['level'] = 1


def practice(data):
    for book in data:
        cards = book['cards']
        random.shuffle(cards)
        rounds = 0
        while any([card['date'] <= date.today() for card in cards]):
            if rounds == 0:
                print('----------------------------------------------------------------------')
                print(book['title'])

            for card in cards:
                if card['date'] <= date.today():
                    successful = present_card(card)
                    update_card(card, successful)
                    print('')

            rounds += 1
            



if __name__ == '__main__':
    data = load_json(json_path)
    practice(data)
    save_json(data, json_path)
