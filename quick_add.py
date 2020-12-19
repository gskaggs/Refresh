import tkinter as tk
from card_utils import total_cards_due


class QuickAddView(tk.Frame):
    def __init__(self, master, close=lambda: None):
        tk.Frame.__init__(self, master)
        self.close = close
        self.type = tk.IntVar()
        self.create_widgets()
        self.pack(side="top", fill="both", expand=True)


    def view_will_appear(self, data):
        self.type = tk.IntVar()

    def create_widgets(self):
        frame_header = tk.Frame(self)
        button_home = tk.Button(frame_header, text="End Session", command=lambda: self.close())
        button_home.pack(side="left")
        frame_header.pack(side="top", fill="x", expand=False, pady=10)

        frame_types = tk.Frame(self)
        tk.Radiobutton(frame_types, text="Python", padx = 20, variable=self.type, value=1).pack(side='left')
        frame_types.pack(side="top", fill="x", expand=False)

        self.btn_submit = tk.Button(self, text='Add card', command=lambda: print(self.type))
        self.btn_submit.pack(fill='x', side=tk.TOP, expand=False, padx=50, pady=5)



if __name__ == "__main__":
    root = tk.Tk()
    main = QuickAddView(root)
    main.view_will_appear([{}, []])
    root.wm_geometry("400x400")
    root.mainloop()