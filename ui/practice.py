import tkinter as tk


class PracticeView(tk.Frame):
    def __init__(self, master, close=None):
        tk.Frame.__init__(self, master)
        self.close = close
        self.create_widgets()
        self.pack(side="top", fill="both", expand=True)


    def create_widgets(self):
        frame_header = tk.Frame(self)
        frame_buttons = tk.Frame(self)
        label_quote = tk.Label(self, text='label_quote')

        frame_header.pack(side="top", fill="x", expand=False)
        label_quote.pack(side="top", fill="both", expand=True)
        frame_buttons.pack(side="top", fill="x", expand=False)
        
        label_progress = tk.Label(frame_header, text='Question X of Y')
        button_home = tk.Button(frame_header, text="End Session", command=lambda: self.close())

        button_home.pack(side="left")
        label_progress.pack(side="right", padx=15)

        button_fail = tk.Button(frame_buttons, text="F", command=lambda: print('X'))
        button_pass = tk.Button(frame_buttons, text="P", command=lambda: print('Y'))

        button_fail.pack(side='left', fill='x', pady=10, padx=10, expand=True)
        button_pass.pack(side='left', fill='x', pady=10, padx=10, expand=True)


if __name__ == "__main__":
    root = tk.Tk()
    main = PracticeView(root)
    root.wm_geometry("400x400")
    root.mainloop()