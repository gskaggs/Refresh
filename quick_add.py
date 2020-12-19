import tkinter as tk
from card_utils import note_card, quote_card, flash_card


class QuickAddView(tk.Frame):
    def __init__(self, master, close=lambda: None):
        tk.Frame.__init__(self, master)
        self.close = close
        self.cards = []
        self.type = tk.IntVar()
        self.type.set(1)
        self.create_widgets()
        self.pack(side="top", fill="both", expand=True)


    def view_will_appear(self, data):
        self.cards = []


    def submit(self):
        raw = self.text.get('1.0', tk.END)[:-1]
        if len(raw) == 0:
            return

        card = None
        if self.type.get() == 1:
            card = quote_card(raw)
        elif self.type.get() == 2:
            card = note_card(raw)
        else:
            raw = raw.split('\n')
            front, back = raw[0], '\n'.join(raw[1:])
            card = flash_card(front, back)
        self.cards.append(card)
        self.text.delete('1.0', tk.END)

    def create_widgets(self):
        frame_header = tk.Frame(self)
        button_home = tk.Button(frame_header, text="Home / Save", command=lambda: self.close())
        button_home.pack(side="left")
        frame_header.pack(side="top", fill="x", expand=False, pady=10)

        frame_types = tk.Frame(self)
        tk.Radiobutton(frame_types, text="Quote",     variable=self.type, padx=10, value=1).pack(side='left', expand=True)
        tk.Radiobutton(frame_types, text="Note",      variable=self.type, padx=10, value=2).pack(side='left', expand=True)
        tk.Radiobutton(frame_types, text="Flashcard", variable=self.type, padx=10, value=3).pack(side='left', expand=True)
        frame_types.pack(side="top", fill="x", expand=False, padx = 20)

        self.text = tk.Text(self, height=20)
        self.text.pack(side='top', fill='x', padx=20, pady=10, expand=False)

        self.btn_submit = tk.Button(self, text='Add card', command=lambda: self.submit())
        self.btn_submit.pack(fill='x', side='top', expand=False, padx=50, pady=(5, 10))



if __name__ == "__main__":
    root = tk.Tk()
    main = QuickAddView(root)
    main.view_will_appear([{}, []])
    root.wm_geometry("400x400")
    root.mainloop()