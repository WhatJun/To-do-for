import tkinter as tk
from tkinter import ttk
import pandas as pd

EVENTPATH = "./record/events.csv"
SCOREPATH = "./record/score.json"
HISGETPATH = "./record/history_get.csv"
HISPAYPATH = "./record/history_pay.csv"
FONT = "YuGothinc"


class History():
    def __init__(self, root, HISGETPATH, HISPAYPATH, FONT="YuGothic"):
        self.root = root
        self.root.title("History")
        self.root.geometry("1200x500")
        self.root.configure(bg="white")
        
        self.font = FONT

        self.HisGet = pd.read_csv(HISGETPATH)
        self.HisPay = pd.read_csv(HISPAYPATH)

        self.create_widgets()

    def create_widgets(self):
        self.frameHisGet = tk.Frame(self.root, bg="white", relief="solid")
        self.frameHisPay = tk.Frame(self.root, bg="gray", relief="solid")

        self.frameHisGet.pack(side="left", fill="both", expand=True)
        self.frameHisPay.pack(side="right", fill="both", expand=True)

        self.labelHisGet = tk.Label(self.frameHisGet, text="Gained", font=(self.font, 20), bg=None)
        self.labelHisPay = tk.Label(self.frameHisPay, text="Redeemed", font=(self.font, 20), bg=None)
        self.labelHisGet.pack()
        self.labelHisPay.pack()

        self.tree = ttk.Treeview(self.frameHisGet)
        self.tree["column"] = ("Event", "Score", "Date")
        self.tree["show"] = "headings"        
        self.tree.heading("Event", text="Prize", anchor="center")
        self.tree.heading("Score", text="Score", anchor="center")
        self.tree.heading("Date", text="Date", anchor="center")
        self.tree.column("Event")
        self.tree.column("Score", anchor="center")
        self.tree.column("Date")
        for i in range(len(self.HisGet)):
            self.tree.insert("", "end", values=list(self.HisGet.iloc[i])) 
        self.tree.pack()

        self.tree = ttk.Treeview(self.frameHisPay)
        self.tree["column"] = ("Event", "Score", "Date")
        self.tree["show"] = "headings"        
        self.tree.heading("Event", text="Prize", anchor="center")
        self.tree.heading("Score", text="Score", anchor="center")
        self.tree.heading("Date", text="Date", anchor="center")
        self.tree.column("Event")
        self.tree.column("Score", anchor="center")
        self.tree.column("Date")
        for i in range(len(self.HisPay)):
            self.tree.insert("", "end", values=list(self.HisPay.iloc[i])) 
        self.tree.pack()


if __name__ == "__main__":
    root = tk.Tk()
    History(root, HISGETPATH, HISPAYPATH)
    root.mainloop()