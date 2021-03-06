import tkinter as tk
from utils.io_utils import save_data, json_path
from practice import PracticeView
from home import HomeView
from quick_add import QuickAddView

# Organizes the various windows of the app
class MainView(tk.Frame):
    def __init__(self, master, data):
        tk.Frame.__init__(self, width=800,height=500)
        self.data = data
        self.user_data, self.book_data = data
        self.create_views()
        self.create_control_flow()
        self.show_home()


    def show_home(self):
        self.home_view.view_will_appear(self.data)
        self.home_view.lift()


    def start_practice(self):
        self.practice_view.view_will_appear(self.data)
        self.practice_view.lift()


    def start_quick_add(self):
        self.quick_add_view.view_will_appear(self.data)
        self.quick_add_view.lift()


    def end_practice(self):
        save_data(self.user_data, self.book_data, json_path)
        self.show_home()


    def end_quick_add(self):
        self.book_data.extend(self.quick_add_view.get_data())
        save_data(self.user_data, self.book_data, json_path)
        self.show_home()


    def create_control_flow(self):
        self.home_view.start_practice = lambda: self.start_practice()
        self.home_view.start_quick_add = lambda: self.start_quick_add()
        self.practice_view.close = lambda: self.end_practice()
        self.quick_add_view.close = lambda: self.end_quick_add()


    def create_views(self):
        self.practice_view = PracticeView(self)
        self.home_view = HomeView(self)
        self.quick_add_view = QuickAddView(self)

        self.practice_view.place(x=0, y=0, relwidth=1, relheight=1)
        self.home_view.place(x=0, y=0, relwidth=1, relheight=1)
        self.quick_add_view.place(x=0, y=0, relwidth=1, relheight=1)