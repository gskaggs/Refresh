import random
from datetime import date, timedelta
from io_utils import save_data, json_path
from card_utils import total_cards_due, book_cards_due, get_cards_due

class PracticeController:
    def __init__(self, data):
        self.user_data, self.book_data = data
        self.session_length = self.user_data.get('session_length', 10)
        random.shuffle(self.book_data)


    def update_card(self, successful):
        print(successful)


    def next_card(self):
        return ('front', 'back')