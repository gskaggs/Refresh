#! /usr/bin/python3

import random
from datetime import date, timedelta
from io_utils import load_data, save_data, json_path
from card_utils import total_cards_due, book_cards_due, get_cards_due

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
        return ('"' + generate_front(quote) + '"', '"' + quote + '"')

    if card_type == 'note':
        note = card['note']
        return (generate_front(note), note)


def present_card(card):
    front, back = get_front_back(card)
    
    responses = []
    responses.append(input(front + '\n'))
    responses.append(input(back +  '\n'))
    successful = all([response.lower().strip() != 'f' for response in responses])
    update_card(card, successful)
    return successful


def update_card(card, successful):
    level_to_days = {1: 1, 2: 3, 3: 7, 4: 14, 5: 21}
    level = card['level']
    if successful:
        card['date'] = date.today() + timedelta(days=level_to_days[level])
        card['level'] = min(card['level'] + 1, 5)
    else:
        card['level'] = 1


def practice(user_data, book_data):
    session_length = user_data.get('session_length', 10)
    card_count = 0

    random.shuffle(book_data)

    for book in book_data:
        if card_count >= session_length:
            break
        
        if book_cards_due(book) == 0:
            continue
        
        print('----------------------------------------------------------------------')
        print(book['title'], '\n')
        
        cards = get_cards_due(book['cards'], session_length - card_count)
        card_count += len(cards)
        random.shuffle(cards)
        
        while len(cards) > 0:
            repeat = []
            for card in cards:
                successful = present_card(card)
                if not successful:
                    repeat.append(card)
                print('')
            cards = repeat


if __name__ == '__main__':
    print('This script is archived and only included if someone wants to develop on it.')
    exit()
    user_data, book_data = load_data(json_path)
    session_length = user_data.get('session_length', 10)
    user_name = user_data.get('user_name', '')
    print('\nHello', user_name + ', let\'s begin.\n')
    total_cards = total_cards_due(book_data)
    print('Total cards due:', total_cards)
    print('Session length:', min(total_cards, session_length), 'cards\n')
    practice(user_data, book_data)
    save_data(user_data, book_data, json_path)