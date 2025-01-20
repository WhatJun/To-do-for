import tkinter as tk
from tkinter import ttk
import pandas as pd
import json
import datetime

EVENTPATH = "./record/events.csv"
SCOREPATH = "./record/score.json"
HISGETPATH = "./record/history_get.csv"
HISPAYPATH = "./record/history_pay.csv"
FONT = "YuGothinc"


class ViewScorer():
    def __init__(self, root, EVENTPATH, SCOREPATH, HISPATH, FONT="YuGothic"):
        self.root = root
        self.root.title("Check Scorer")
        self.root.geometry("600x500+500+200")
        self.root.configure(bg="white")
        
        self.csv = pd.read_csv(EVENTPATH)
        self.scorepath = SCOREPATH
        with open(self.scorepath, "r") as file:
            self.score = json.load(file)        
        self.history = pd.read_csv(HISPATH)
        self.hispath = HISPATH

        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root, bg="white", relief="solid", bd=1)
        frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5) # フレームの設定と配置
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)

        self.menu = tk.Menu(frame, tearoff=0, activebackground="#000000")
        self.menu.add_command(label="Count", command=self.count_score)
        self.root.bind("<Button-2>", self.show_menu) # 右クリックによるメニュー表示をバインド

        self.tree = ttk.Treeview(frame)
        self.tree["column"] = ("Event", "Score")
        self.tree["show"] = "headings"
        
        self.tree.heading("Event", text="Event", anchor="center")
        self.tree.heading("Score", text="Score", anchor="center")

        self.tree.column("Event", width=300)
        self.tree.column("Score", width=100, anchor="center")

        for i in range(len(self.csv)):
            self.tree.insert("", "end", values=list(self.csv.iloc[i]))
        self.tree.grid(row=0, column=0, sticky=tk.W + tk.E + tk.N + tk.S)

        vscrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=lambda:self.tree.yview)
        self.tree.configure(yscrollcommand=vscrollbar.set) # スクロールバー設定
        vscrollbar.grid(row=0, column=1, sticky=tk.W + tk.E + tk.N + tk.S)
        
        
    def show_menu(self, e):
        region = self.tree.identify_region(e.x, e.y)
        
        if region == "cell": # クリックされたのがセルの場合
            self.tree.selection_set(self.tree.identify_row(e.y)) # クリックされた行を選択
            self.menu.post(e.x_root, e.y_root) # メニューを表示

    def count_score(self):
        selected = self.tree.selection()
        if selected:
            item = self.tree.item(selected)
            event = item["values"][0]
            score = float(item["values"][1])
            
            # スコアを加算
            self.score["score"] = self.score.get("score", 0) + score
            
            # スコアの変更をJSONファイルに保存
            with open(self.scorepath, "w") as file:
                json.dump(self.score, file, ensure_ascii=False)

            # 履歴に追加
            date = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
            new_row = pd.DataFrame({"Event": [event], "Score": [score], "Date": [date]})
            self.history = pd.concat([self.history, new_row], ignore_index=True)
            
            # 履歴CSVに保存
            self.history.to_csv(self.hispath, index=False)

if __name__ == "__main__":
    root = tk.Tk()
    ViewScorer(root, EVENTPATH, SCOREPATH, HISGETPATH)
    root.mainloop()