import tkinter as tk
from tkinter import ttk
import pandas as pd

HISGETPATH = "./record/history_get.csv"
HISPAYPATH = "./record/history_pay.csv"
FONT = "YuGothic"


class History:
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
        # Frames for the two sections
        self.frameHisGet = tk.Frame(self.root, bg="white", relief="solid", bd=1)
        self.frameHisPay = tk.Frame(self.root, bg="white", relief="solid", bd=1)

        self.frameHisGet.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.frameHisPay.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        # Add weight to rows and columns
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        ''' 
        Gained (HisGet)
        '''
        self.labelHisGet = tk.Label(self.frameHisGet, text="Gained", font=(self.font, 20), bg="white")
        self.labelHisGet.pack(anchor="w", pady=5)

        self.treeHisGet = ttk.Treeview(self.frameHisGet, columns=("Event", "Score", "Date"), show="headings")
        self.treeHisGet.heading("Event", text="Prize", anchor="center")
        self.treeHisGet.heading("Score", text="Score", anchor="center")
        self.treeHisGet.heading("Date", text="Date", anchor="center")
        self.treeHisGet.column("Event", width=150, anchor="w")
        self.treeHisGet.column("Score", width=100, anchor="center")
        self.treeHisGet.column("Date", width=150, anchor="center")

        # Populate the table
        for i in range(len(self.HisGet)):
            color = "plus" if self.HisGet.iloc[i, 1] >= 0 else "minus"
            self.treeHisGet.insert("", "end", values=list(self.HisGet.iloc[i]), tags=color)

        self.treeHisGet.tag_configure("plus", background="white", foreground="blue")
        self.treeHisGet.tag_configure("minus", background="white", foreground="red")
        
        self.treeHisGet.pack(fill="both", expand=True, side="left")

        # Add scrollbar
        vscrollHisGet = ttk.Scrollbar(self.frameHisGet, orient="vertical", command=self.treeHisGet.yview)
        self.treeHisGet.configure(yscrollcommand=vscrollHisGet.set)
        vscrollHisGet.pack(side="right", fill="y")

        ''' 
        Redeemed (HisPay)
        '''
        self.labelHisPay = tk.Label(self.frameHisPay, text="Redeemed", font=(self.font, 20), bg="white")
        self.labelHisPay.pack(anchor="w", pady=5)

        self.treeHisPay = ttk.Treeview(self.frameHisPay, columns=("Event", "Score", "Date"), show="headings")
        self.treeHisPay.heading("Event", text="Prize", anchor="center")
        self.treeHisPay.heading("Score", text="Score", anchor="center")
        self.treeHisPay.heading("Date", text="Date", anchor="center")
        self.treeHisPay.column("Event", width=150, anchor="w")
        self.treeHisPay.column("Score", width=100, anchor="center")
        self.treeHisPay.column("Date", width=150, anchor="center")

        # Populate the table
        for i in range(len(self.HisPay)):
            self.treeHisPay.insert("", "end", values=list(self.HisPay.iloc[i]))

        self.treeHisPay.pack(fill="both", expand=True, side="left")

        # Add scrollbar
        vscrollHisPay = ttk.Scrollbar(self.frameHisPay, orient="vertical", command=self.treeHisPay.yview)
        self.treeHisPay.configure(yscrollcommand=vscrollHisPay.set)
        vscrollHisPay.pack(side="right", fill="y")


if __name__ == "__main__":
    root = tk.Tk()
    History(root, HISGETPATH, HISPAYPATH)
    root.mainloop()
