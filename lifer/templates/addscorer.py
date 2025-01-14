import tkinter as tk
import pandas as pd

EVENTPATH = "./record/events.csv"
SCOREPATH = "./record/score.json"
SHOPPATH = "./record/shoplist.csv"
HISGETPATH = "./record/history_get.csv"
HISPAYPATH = "./record/history_pay.csv"
FONT = "YuGothinc"


class AddScorer():
    def __init__(self, root, EVENTPATH, FONT="YuGothic"):
        self.root = root
        self.root.title("Add Scorer")
        self.root.geometry("300x200+500+300")
        self.root.configure(bg="white")
        
        self.csvpath = EVENTPATH
        self.font = FONT

        self.create_widgets()


    def create_widgets(self):
        self.label_event = tk.Label(self.root, text="Event", font=(self.font, 12), bg="white")
        self.entry_event = tk.Entry(self.root, font=(self.font, 12), bg="#f5c6ef")
        self.label_score = tk.Label(self.root, text="Score", font=(self.font, 12), bg="white")
        self.entry_score = tk.Entry(self.root, font=(self.font, 12), bg="#f5c6ef")
        self.button_add = tk.Button(self.root, text="Add", font=(self.font, 12), bg="white", command=self.add_scorer)
        self.button_quit = tk.Button(self.root, text="Quit", font=(self.font, 12), bg="white", command=self.quit)

        self.label_event.pack()
        self.entry_event.pack()
        self.label_score.pack()
        self.entry_score.pack()
        self.button_add.pack()
        self.button_quit.pack()

    def add_scorer(self):
        event = self.entry_event.get()
        score = self.entry_score.get()

        content = pd.DataFrame({           
            "Event": [event],
            "Score": [score]
        })

        content.to_csv(self.csvpath, mode="a", header=False, index=False)

        self.entry_event.delete(0, tk.END)
        self.entry_score.delete(0, tk.END)

    def quit(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    AddScorer(root, EVENTPATH)
    root.mainloop()