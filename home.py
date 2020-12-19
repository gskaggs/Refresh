import tkinter as tk
from card_utils import total_cards_due


class HomeView(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.start_practice = lambda: None
        self.start_quick_add = lambda: None
        self.create_widgets()
        self.pack(side="top", fill="both", expand=True, pady=75)

    def view_will_appear(self, data):
        _, book_data = data
        total_due = total_cards_due(book_data)
        self.lbl_progress.config(text='%d cards due today' % total_due)
        btn_practice_state = tk.NORMAL if total_due > 0 else tk.DISABLED
        self.btn_practice.config(state=btn_practice_state)

    def create_widgets(self):
        self.lbl_greeting = tk.Label(self, text='Hello Mr. Skaggs, let\'s get started.')
        self.lbl_greeting.pack(fill=tk.BOTH, side=tk.TOP, expand=False, padx=5, pady=(20, 10))

        self.btn_practice = tk.Button(self, text='Practice!', command=lambda: self.start_practice())
        self.btn_practice.pack(fill='x', side=tk.TOP, expand=False, padx=50, pady=5)

        self.btn_add_cards = tk.Button(self, text='Add cards', command=lambda: self.start_quick_add())
        self.btn_add_cards.pack(fill='x', side=tk.TOP, expand=False, padx=50, pady=5)

        self.lbl_progress = tk.Label(self, text='')
        self.lbl_progress.pack(fill='x', side=tk.BOTTOM, expand=False, padx=50, pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    main = HomeView(root)
    root.wm_geometry("400x400")
    root.mainloop()