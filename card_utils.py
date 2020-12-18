from datetime import date, timedelta
import random

def book_cards_due(book):
    return sum([1 if card['date'] <= date.today() else 0 for card in book['cards']])


def total_cards_due(data):
    return sum([book_cards_due(book) for book in data])


def get_cards_due(cards, limit):
    due = [card for card in cards if card['date'] <= date.today()]
    return due[:min(len(due), limit)]


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


def update_card(card, successful):
    level_to_days = {1: 1, 2: 3, 3: 7, 4: 14, 5: 21}
    level = card['level']
    if successful:
        card['date'] = date.today() + timedelta(days=level_to_days[level])
        card['level'] = min(card['level'] + 1, 5)
    else:
        card['level'] = 1


def generate_card_stack(book_data, session_length):
    stack = []
    random.shuffle(book_data)
    for book in book_data:
        if len(stack) > session_length:
            break
        random.shuffle(book['cards'])
        cards = get_cards_due(book['cards'], session_length - len(stack))
        stack.extend(cards)
    return stack


def vanilla_card():
    card = {}
    card['level'] = 1
    card['date']  = date.today()
    return card


def note_card(note):
    card = vanilla_card()
    card['note'] = note
    card['type']  = 'note'
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
