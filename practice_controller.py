import random
from utils.card_utils import total_cards_due, generate_card_stack, update_card, get_front_back, hash_card

# Controls the internal logic for the practice view
class PracticeController:
    def __init__(self, data):
        self.user_data, self.book_data = data
        total_due = total_cards_due(self.book_data)
        self.session_length = min(self.user_data.get('session_length', 10), total_due)
        self.progress_count = 0

        self.card_stack, self.card_titles = generate_card_stack(self.book_data, self.session_length)
        self.repeat = []


    def get_cur_title(self):
        return self.card_titles[hash_card(self.cur_card)]


    def get_progress(self):
        return (self.progress_count, self.session_length)


    def update_card(self, successful):
        update_card(self.cur_card, successful)
        if successful:
            self.progress_count += 1
        else:
            self.repeat.append(self.cur_card)


    def next_card(self):
        if len(self.card_stack) == 0 and len(self.repeat) == 0:
            return None
        
        elif len(self.card_stack) == 0:
            self.card_stack = self.repeat
            self.repeat = []

        self.cur_card = self.card_stack.pop()
        return get_front_back(self.cur_card)