from tkinter import *
from tkinter import ttk

class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title("Python Tkinter")
        self.geometry("600x600")
        self.resizable(0, 0)

def main():
    root = Root()
    ttk.Button(root, text="Quit", command = root.destroy).place(x = 200, y = 200)
    root.mainloop()

if __name__ == "__main__":
    main()

"""
TODO
make resizable, learn how to use grid/pack for buttons and such

default screen
options - create new folder, view quotes, view watchlists

libraries - tkinter, market api, statplots, probably math

need a database at some point
"""