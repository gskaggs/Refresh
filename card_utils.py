from datetime import date


def book_cards_due(book):
    return sum([1 if card['date'] <= date.today() else 0 for card in book['cards']])


def total_cards_due(data):
    return sum([book_cards_due(book) for book in data])


def get_cards_due(cards, limit):
    due = [card for card in cards if card['date'] <= date.today()]
    return due[:min(len(due), limit)]


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
