import tkinter as tk
from tkinter import ttk
import pandas as pd
import json
import datetime

EVENTPATH = "./record/events.csv"
SCOREPATH = "./record/score.json"
SHOPPATH = "./record/shoplist.csv"
HISGETPATH = "./record/history_get.csv"
HISPAYPATH = "./record/history_pay.csv"
FONT = "YuGothinc"


class Shop():
    def __init__(self, root, SCOREPATH, SHOPPATH, HISPAYPATH, FONT="YuGothic"):
        self.root = root
        self.root.title("Shop")
        self.root.geometry("600x500+500+200")
        self.root.configure(bg="white")
        
        self.scorepath = SCOREPATH
        with open(self.scorepath, "r") as file:
            self.score = json.load(file)
        self.shoplist = pd.read_csv(SHOPPATH)        
        self.history = pd.read_csv(HISPAYPATH)
        self.hispath = HISPAYPATH
        self.font = FONT

        self.create_widgets()

    def create_widgets(self):
        self.menu = tk.Menu(self.root, tearoff=0, activebackground="#000000")
        self.menu.add_command(label="Redeem", command=self.redeem)
        self.root.bind("<Button-2>", self.show_menu) 

        self.tree = ttk.Treeview(self.root)
        self.tree["column"] = ("Prize", "Score")
        self.tree["show"] = "headings"
        
        self.tree.heading("Prize", text="Prize", anchor="center")
        self.tree.heading("Score", text="Score", anchor="center")

        self.tree.column("Prize", width=300)
        self.tree.column("Score", width=100, anchor="center")


        for i in range(len(self.shoplist)):
            self.tree.insert("", "end", values=list(self.shoplist.iloc[i])) 
        self.tree.pack()
        
    def show_menu(self, e):
        region = self.tree.identify_region(e.x, e.y)
        
        if region == "cell": # クリックされたのがセルの場合
            self.tree.selection_set(self.tree.identify_row(e.y)) # クリックされた行を選択
            self.menu.post(e.x_root, e.y_root) # メニューを表示

    def redeem(self):
        selected = self.tree.selection()
        if selected:
            item = self.tree.item(selected)
            prize = item["values"][0]
            score = float(item["values"][1])

            self.score["score"] = self.score.get("score", 0) - score
            
            # スコアの変更をJSONファイルに保存
            with open(self.scorepath, "w") as file:
                json.dump(self.score, file, ensure_ascii=False)

            # 履歴に追加
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_row = pd.DataFrame({"Prize": [prize], "Score": [score], "Date": [date]})
            self.history = pd.concat([self.history, new_row], ignore_index=True)
            
            # 履歴CSVに保存
            self.history.to_csv(self.hispath, index=False)

if __name__ == "__main__":
    root = tk.Tk()
    Shop(root, SCOREPATH, SHOPPATH, HISPAYPATH)
    root.mainloop()