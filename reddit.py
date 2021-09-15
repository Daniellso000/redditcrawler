import praw
from tkinter import *
import time
raiz=Tk()


class Janela:
    def __init__(self, toplevel):
        self.fr1 = Frame(toplevel)
        self.fr1.pack()


reddit = praw.Reddit(
    client_id="",
    client_secret="",
    password="",
    user_agent="",
    username="",
)



def retrieve_input():
    titulo = []
    inputValue=textBox.get("1.0","end-1c")
    subreddit = reddit.subreddit(inputValue)
    hot_python = subreddit.hot(limit=5)
    subreddit.subscribe()
    for submission in hot_python:
        if not submission.stickied:
            print(titulo)
            titulo.append(submission.title)
    label3 = Label(raiz, text=titulo)
    label3.pack()





textBox=Text(raiz, height=2, width=10)
textBox.pack()

buttonCommit = Button(raiz, height= 1, width = 10, text="Commit", command=lambda: retrieve_input())


buttonCommit.pack()
Janela(raiz)
raiz.mainloop()
