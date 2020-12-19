#! /usr/bin/env python

import tkinter as tk
from main import MainView
from io_utils import load_data, json_path

if __name__ == "__main__":
    data = load_data(json_path)
    root = tk.Tk()
    root.title('')
    root['bg'] = '#222222'
    main = MainView(root, data)
    main.pack(side="top", expand=True)
    root.wm_geometry("800x600")
    root.mainloop()