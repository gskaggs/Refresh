#! /usr/bin/python3

from utils import load_json, save_json, json_path, multiline_input
from datetime import date

def vanilla_card():
    card = {}
    card['level'] = 1
    card['date']  = date.today()
    return card


def quote_card(quote):
    card = vanilla_card()
    card['quote'] = quote
    card['type']  = 'quote'
    return card


def flash_card(front, back):
    card = vanilla_card()
    card['front'] = front
    card['back']  = back
    card['type']  = 'flash'
    return card
    

def get_book_data():
    title  = input('Title:\n')
    thesis = input('Thesis:\n')
    
    defns  = []

    print('Abstractions')
    while True:
        name = input('Name:\n')
        if len(name) == 0:
            break
        defns.append((name, multiline_input('Definition:')))

    notes  = multiline_input('Takeaways:')
    quotes = multiline_input('Quotes:')

    cards = []
    cards.append(flash_card('Thesis', thesis))
    cards.append(flash_card('Takeaways', notes))

    for quote in quotes.split('\n'):
        cards.append(quote_card(quote))
    
    for defn in defns:
        cards.append(flash_card(*defn))

    data = {}
    data['title'] = title
    data['cards'] = cards
    
    return data


def add_book(data):
    book = get_book_data()
    data.append(book)


if __name__ == '__main__':
    data = load_json(json_path)
    add_book(data)
    save_json(data, json_path)


