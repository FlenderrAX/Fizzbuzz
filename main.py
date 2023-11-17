import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

class Button(ttk.Button):
    def __init__(self, container):
        super().__init__(container)

        self.play_button = ImageTk.PhotoImage(Image.open("img/play_button.png"))
        self.config(image=self.play_button, command=self.play)
        self.place(x=0, y=0)

    def play(self):
        pass

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fizzbuzz - A new way to learn more things")
        self.geometry("1066x500")
        self.resizable(False, False)
        self.attributes("-toolwindow", True)

        self.background = ImageTk.PhotoImage(Image.open("img/background.png"))
        self.background_label = tk.Label(self, image=self.background)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.button = Button(self)
        self.button.place(x=533, y=250, anchor="center")


if __name__ == "__main__":
    app = App()
    app.mainloop()