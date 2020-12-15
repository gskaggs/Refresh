#! /usr/bin/env python

import tkinter as tk
from practice import PracticeView
from home import HomeView

class MainView(tk.Frame):
    def __init__(self, master, data):
        print(data)
        tk.Frame.__init__(self)
        self.create_views()
        self.create_control_flow()
        self.home_view.lift()


    def create_control_flow(self):
        self.practice_view.close = lambda: self.home_view.lift() 


    def create_views(self):
        self.practice_view = PracticeView(self)
        self.home_view = HomeView(self, self.practice_view)

        self.practice_view.place(x=0, y=0, relwidth=1, relheight=1)
        self.home_view.place(x=0, y=0, relwidth=1, relheight=1)


if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root, ({}, []))
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()