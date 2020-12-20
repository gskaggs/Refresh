#! /usr/bin/python3

from io_utils import load_data, save_data, json_path, multiline_input
from card_utils import quote_card
    

def get_quote_data():
    author  = input('Author:\n')
    
    quotes = multiline_input('Quotes:')
    cards = []

    for quote in quotes.split('\n'):
        if len(quote) > 0:
            cards.append(quote_card(quote))

    data = {}
    data['title'] = author
    data['cards'] = cards
    
    return data


def add_quotes(data):
    quotes = get_quote_data()
    data.append(quotes)


if __name__ == '__main__':
    print('This script is archived and only included if someone wants to develop on it.')
    exit()
    user_data, book_data = load_data(json_path)
    add_quotes(book_data)
    save_data(user_data, book_data, json_path)


