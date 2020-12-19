import tkinter as tk
from io_utils import load_data, json_path
from practice_controller import PracticeController

class PracticeView(tk.Frame):
    def __init__(self, master, close=lambda: None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.close = close
        self.create_widgets()
        self.pack(side="top", fill="both", expand=True)


    def view_will_appear(self, data):
        self.controller = PracticeController(data)
        first_card = self.controller.next_card()
        if first_card == None:
            self.close()
        self.card_front, self.card_back = first_card
        self.label_quote.config(text=self.card_front)
        self.button_fail.config(state=tk.DISABLED)
        self.button_pass.config(text='N')
        self.reset_progress_bar()
        self.state = 'front'

    def reset_progress_bar(self):
        progress, session_length = self.controller.get_progress()
        self.label_progress.config(text='Question %d of %d' % (progress + 1, session_length))

    def change_sate(self):
        if self.state == 'front':
            self.button_fail.config(state=tk.NORMAL)
            self.button_pass.config(text='P')
            self.label_quote.config(text=self.card_back)
            self.state = 'back'
        elif self.state == 'back':
            self.button_fail.config(state=tk.DISABLED)
            self.button_pass.config(text='N')
            self.state = 'front'
            next_card = self.controller.next_card()
            if next_card == None:
                self.close()
            else:
                self.card_front, self.card_back = next_card
                self.label_quote.config(text=self.card_front)
        
        self.reset_progress_bar()
            

    def button_fail_pressed(self):
        self.controller.update_card(False)
        self.change_sate()


    def button_pass_pressed(self):
        if self.state == 'back':
            self.controller.update_card(True)
        self.change_sate()


    def create_widgets(self):
        frame_header = tk.Frame(self)
        frame_buttons = tk.Frame(self)

        self.label_quote = tk.Label(self, text='', wraplength=300)

        frame_header.pack(side="top", fill="x", expand=False)
        self.label_quote.pack(side="top", fill="both", expand=True)
        frame_buttons.pack(side="top", fill="x", expand=False)
        
        self.label_progress = tk.Label(frame_header, text='Question X of Y')
        button_home = tk.Button(frame_header, text="End Session", command=lambda: self.close())

        button_home.pack(side="left")
        self.label_progress.pack(side="right", padx=15)

        self.button_fail = tk.Button(frame_buttons, state='disabled', text="F", command=lambda: self.button_fail_pressed())
        self.button_pass = tk.Button(frame_buttons, text='N', command=lambda: self.button_pass_pressed())

        self.button_fail.pack(side='left', fill='x', pady=10, padx=10, expand=True)
        self.button_pass.pack(side='left', fill='x', pady=10, padx=10, expand=True)


if __name__ == "__main__":
    data = load_data(json_path)
    root = tk.Tk()
    main = PracticeView(root, data)
    root.wm_geometry("400x400")
    root.mainloop()