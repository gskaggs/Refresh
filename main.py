#! /usr/bin/env python

import tkinter as tk
from practice import PracticeView
from io_utils import save_data, json_path
from home import HomeView

class MainView(tk.Frame):
    def __init__(self, master, data):
        tk.Frame.__init__(self)
        self.data = data
        self.user_data, self.book_data = data
        self.create_views()
        self.create_control_flow()
        self.home_view.view_will_appear(self.data)
        self.home_view.lift()


    def start_practice(self):
        self.practice_view.view_will_appear(self.data)
        self.practice_view.lift()


    def end_practice(self):
        save_data(self.user_data, self.book_data, json_path)
        self.home_view.view_will_appear(self.data)
        self.home_view.lift()


    def create_control_flow(self):
        self.home_view.start_practice = lambda: self.start_practice()
        self.practice_view.close = lambda: self.end_practice()


    def create_views(self):
        self.practice_view = PracticeView(self)
        self.home_view = HomeView(self, self.practice_view)

        self.practice_view.place(x=0, y=0, relwidth=1, relheight=1)
        self.home_view.place(x=0, y=0, relwidth=1, relheight=1)