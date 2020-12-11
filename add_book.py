#! /usr/bin/python3

from io_utils import load_json, save_json, json_path, multiline_input
from card_utils import note_card, quote_card, flash_card
    

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

    for note in notes.split('\n'):
        if len(note) > 0:
            cards.append(note_card(note))

    for quote in quotes.split('\n'):
        if len(quote) > 0:
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


