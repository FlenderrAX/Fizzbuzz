import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fizzbuzz - A new way to learn more things")
        self.geometry("500x500")
        self.resizable(False, False)
        self.attributes("-toolwindow", True)

if __name__ == "__main__":
    app = App()
    app.mainloop()