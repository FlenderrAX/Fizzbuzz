import tkinter as tk
from tkinter import ttk
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
    def __init__(self, container, image_path, command=None):
        super().__init__(container)
        self.image = ImageTk.PhotoImage(Image.open(image_path))
        self.config(image=self.image, command=command)

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

        self.button = Button(self, "img/play_button.png", self.play)
        self.button.place(x=533, y=250, anchor="center")

        self.good_answers = 0
        self.bad_answers = 0

    def play(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.background_label = tk.Label(self, image=self.background)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        with open('save.json', 'r') as f:
            data = json.load(f)

        questions = [Question(**q) for q in data['questions']]
        random_question = random.choice(questions)

        question_label = tk.Label(self, text=random_question.question, font=("Arial", 13), bg="#ffffff")
        question_label.place(x=533, y=250, anchor="center")
        
        self.correct_answer_button = ttk.Button(self, text=random_question.answer, command=lambda: self.answer(True))
        self.correct_answer_button.place(x=533, y=300, anchor="center")

        self.wrong_answer_button = ttk.Button(self, text=random_question.wrong_answer, command=lambda: self.answer(False))
        self.wrong_answer_button.place(x=533, y=350, anchor="center")

        self.good_answers_count = tk.Label(self, text=f"Good answers: {self.good_answers}", font=("Arial", 13), bg="#ffffff")
        self.good_answers_count.place(x=0, y=0)

        self.result_label = tk.Label(self, font=("Arial", 13), bg="#ffffff")
        self.result_label.place(x=533, y=400, anchor="center")


        self.time_left = 10
        self.countdown_label = tk.Label(self, text=f"Time left: {self.time_left}", font=("Arial", 13), bg="#ffffff")
        self.countdown_label.place(x=533, y=450, anchor="center")
        self.countdown()

    def countdown(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.countdown_label.config(text=f"Time left: {self.time_left}")
            self.after(1000, self.countdown)
        else:
            self.answer(False)

    def answer(self, is_correct):
        self.time_left = 0

        self.correct_answer_button.config(state='disabled')
        self.wrong_answer_button.config(state='disabled')

        if is_correct:
            self.result_label.config(text="You are correct!", fg="green")
            self.good_answers += 1
            self.good_answers_count.config(text=f"Good answers: {self.good_answers}")
        else:
            self.result_label.config(text="You are wrong!", fg="red")
            self.bad_answers += 1

        self.after(2000, self.play)

if __name__ == "__main__":
    app = App()
    app.mainloop()