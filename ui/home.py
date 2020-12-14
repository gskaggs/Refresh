import tkinter as tk

def practice():
    print('hello')


class HomeView(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.create_widgets()
        self.pack(side="top", fill="both", expand=True, pady=75)


    def create_widgets(self):
        lbl_greeting = tk.Label(self, text='Hello Mr. Skaggs, let\'s get started.')
        lbl_greeting.pack(fill=tk.BOTH, side=tk.TOP, expand=False, padx=5, pady=10)

        btn_practice = tk.Button(self, text='Practice!', command=practice)
        btn_practice.pack(fill='x', side=tk.TOP, expand=False, padx=50, pady=5)

        btn_practice = tk.Button(self, text='Add cards', command=practice)
        btn_practice.pack(fill='x', side=tk.TOP, expand=False, padx=50, pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    main = HomeView(root)
    root.wm_geometry("400x400")
    root.mainloop()