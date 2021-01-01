import tkinter as tk
from utils.io_utils import load_data, json_path
from practice_controller import PracticeController
import tkinter.font as tkFont

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
        self.lbl_quote.config(text=self.card_front, font=tkFont.Font(size=20))
        self.btn_fail.config(state=tk.DISABLED)
        self.btn_pass.config(text='Flip')
        self.lbl_title.config(text=self.controller.get_cur_title())
        self.reset_progress_bar()
        self.state = 'front'


    def reset_progress_bar(self):
        progress, session_length = self.controller.get_progress()
        self.lbl_progress.config(text='Question %d of %d' % (progress + 1, session_length))


    def change_sate(self):
        if self.state == 'front':
            self.btn_fail.config(state=tk.NORMAL)
            self.btn_pass.config(text='Pass')
            font = tkFont.Font(size=20) if len(self.card_back) < 225 else tkFont.Font(size=14)
            self.lbl_quote.config(text=self.card_back, font=font)
            self.state = 'back'
        elif self.state == 'back':
            self.btn_fail.config(state=tk.DISABLED)
            self.btn_pass.config(text='Flip')
            self.state = 'front'
            next_card = self.controller.next_card()
            if next_card == None:
                self.close()
            else:
                self.card_front, self.card_back = next_card
                self.lbl_quote.config(text=self.card_front, font=tkFont.Font(size=20))
        
        self.reset_progress_bar()
        self.lbl_title.config(text=self.controller.get_cur_title())
            

    def btn_fail_pressed(self):
        self.controller.update_card(False)
        self.change_sate()


    def btn_pass_pressed(self):
        if self.state == 'back':
            self.controller.update_card(True)
        self.change_sate()


    def create_widgets(self):
        frame_header = tk.Frame(self)
        frame_buttons = tk.Frame(self)

        self.lbl_title = tk.Label(self, text='')
        self.lbl_quote = tk.Label(self, text='', wraplength=300, font=tkFont.Font(size=20))

        frame_header.pack(side="top", fill="x", expand=False, pady=5)
        self.lbl_quote.pack(side="top", fill="both", pady=(60,0), expand=True)
        self.lbl_title.pack(side="top", pady=(0,60))
        frame_buttons.pack(side="top", fill="x", expand=False)
        
        self.lbl_progress = tk.Label(frame_header, text='Question X of Y')
        btn_home = tk.Button(frame_header, text="End Session", command=lambda: self.close())

        btn_home.pack(side="left", padx=10)
        self.lbl_progress.pack(side="right", padx=15)

        self.btn_fail = tk.Button(frame_buttons, state='disabled', text="Fail", command=lambda: self.btn_fail_pressed())
        self.btn_pass = tk.Button(frame_buttons, text='Next', command=lambda: self.btn_pass_pressed())

        self.btn_fail.pack(side='left', fill='x', pady=10, padx=10, expand=True)
        self.btn_pass.pack(side='left', fill='x', pady=10, padx=10, expand=True)


# Used for testing
if __name__ == "__main__":
    data = load_data(json_path)
    root = tk.Tk()
    main = PracticeView(root, data)
    root.wm_geometry("400x400")
    root.mainloop()