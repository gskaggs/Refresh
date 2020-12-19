#! /usr/bin/env python

import tkinter as tk
from main import MainView
from io_utils import load_data, json_path

if __name__ == "__main__":
    data = load_data(json_path)
    root = tk.Tk()
    root.title('')
    main = MainView(root, data)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()