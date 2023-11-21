import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import json

class Question:
    def __init__(self, index, question, answer, wrong_answer):
        self.index = index
        self.question = question
        self.answer = answer
        self.wrong_answer = wrong_answer

class Button(ttk.Button):
    def __init__(self, container):
        super().__init__(container)

        self.play_button = ImageTk.PhotoImage(Image.open("img/play_button.png"))
        self.config(image=self.play_button)
        self.place(x=0, y=0)

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
        self.button["command"] = self.play
        self.button.place(x=533, y=250, anchor="center")

    def play(self):
        for widget in app.winfo_children():
            widget.destroy()
        self.play_background = ImageTk.PhotoImage(Image.open("img/background.png"))
        self.play_background_label = tk.Label(self, image=self.background)
        self.play_background_label.place(x=0, y=0, relwidth=1, relheight=1)
        with open('save.json', 'r') as f:
            data = json.load(f)

        questions = [Question(**q) for q in data['questions']]
        random_question = random.choice(questions)

        question_label = tk.Label(self, text=random_question.question, font=("Arial", 13), bg="#ffffff")
        question_label.place(x=533, y=250, anchor="center")
        
        correct_answer_button = ttk.Button(self, text=random_question.answer, command=self.correct_answer)
        correct_answer_button.place(x=533, y=300, anchor="center")

        wrong_answer_button = ttk.Button(self, text=random_question.wrong_answer, command=self.wrong_answer)
        wrong_answer_button.place(x=533, y=350, anchor="center")

    def correct_answer(self):
        messagebox.showinfo("Correct", "You are correct!")

    def wrong_answer(self):
        messagebox.showerror("Wrong", "You are wrong!")


if __name__ == "__main__":
    app = App()
    app.mainloop()