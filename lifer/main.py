import tkinter as tk
import pandas as pd
import json
import os

from templates import *

parent_dir = os.path.dirname(__file__)
EVENTPATH = os.path.join(parent_dir, "record", "events.csv")
SCOREPATH = os.path.join(parent_dir, "record", "score.json")
SHOPPATH = os.path.join(parent_dir, "record", "shoplist.csv")
HISGETPATH = os.path.join(parent_dir, "record", "history_get.csv")
HISPAYPATH = os.path.join(parent_dir, "record", "history_pay.csv")
FONT = "YuGothinc"


class Main():
    def __init__(self, root):
        self.root = root
        self.root.title("Main")
        self.root.geometry("800x500+500+300")
        self.root.configure(bg="white")


        self.eventpath = EVENTPATH
        with open(SCOREPATH, "r") as file:
            self.scorefile = json.load(file)

        self.create_widgets()
        
        
    def create_widgets(self):
        self.frame_score = tk.Frame(self.root, bg="#e6e6fa", height=20, relief="solid")
        self.frame_menu = tk.Frame(self.root, bg="white", relief="solid")
        self.frame_mission = tk.Frame(self.root, bg="white", relief="solid")
        self.frame_bottom = tk.Frame(self.root, bg="#afeeee", relief="solid")

        self.frame_score.pack(side="top", fill="both", expand=False)
        self.frame_menu.pack(side="left", fill="both", expand=False)
        self.frame_mission.pack(side="right")
        self.frame_bottom.pack(side="bottom")

        self.label_score = tk.Label(self.frame_score, text="Score:", font=(FONT, 30), bg=None)
        self.score = tk.Label(self.frame_score, font=(FONT, 20), bg=None)
        self.score.config(text=self.scorefile["score"])
        self.refresh = tk.Button(self.frame_score, text="Refresh", font=(FONT, 20), bg=None, command=self.refresh_score)
        self.button_add = tk.Button(self.frame_menu, text="Add Scorer", font=(FONT, 20), bg=None, command=lambda: self.open_AddScorer(), width=20)
        self.button_check = tk.Button(self.frame_menu, text="Check Scorer", font=(FONT, 20), bg=None, command=lambda: self.open_ViewScorer(), width=20)
        self.button_shop = tk.Button(self.frame_menu, text="Shop", font=(FONT, 20), bg=None, command=lambda: self.open_Shop(), width=20)
        self.button_history = tk.Button(self.frame_menu, text="History", font=(FONT, 20), bg=None, command=lambda: self.open_History(), width=20)
        self.button_quit = tk.Button(self.frame_bottom, text="Quit", font=(FONT, 20), bg=None, command=self.quit, width=20)

        self.label_score.pack()
        self.score.pack()
        self.refresh.pack()
        self.button_add.pack()
        self.button_check.pack()
        self.button_shop.pack()
        self.button_history.pack()
        self.button_quit.pack()

    def refresh_score(self):
        with open(SCOREPATH, "r") as file:
            self.scorefile = json.load(file)
        self.score.config(text=self.scorefile["score"])

    def open_AddScorer(self):
        self.win = tk.Toplevel(self.root)
        self.window = AddScorer(self.win, EVENTPATH, FONT)
    
    def open_ViewScorer(self):
        self.win = tk.Toplevel(self.root)
        self.window = ViewScorer(self.win, EVENTPATH, SCOREPATH, HISGETPATH)
    
    def open_Shop(self):
        self.win = tk.Toplevel(self.root)
        self.window = Shop(self.win, SCOREPATH, SHOPPATH, HISPAYPATH)
    
    def open_History(self):
        self.win = tk.Toplevel(self.root)
        self.window = History(self.win, HISGETPATH, HISPAYPATH)

    def quit(self):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    Main(root)
    root.mainloop()