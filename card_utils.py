from datetime import date


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
