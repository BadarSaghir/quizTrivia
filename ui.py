THEME_COLOR = "#375362"
from tkinter import *

class  QuizUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score_label = Label(text="Score: 0", fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.canvas= Canvas(width=300, height=250, bg="White")
        self.question_text = self.canvas.create_text(150,125,text="Some quesion text", fill=THEME_COLOR,font=("Arial",20,"italic"))
        self.canvas.grid(row=1, column=0, columnspan=3,pady=20,padx=10)
        true_img = PhotoImage(file="./images/true.png")
        false_img = PhotoImage(file="./images/false.png")
        self.true_button = Button(image=true_img, highlightthickness=0)
        self.false_button = Button(image=false_img, highlightthickness=0)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self.window.mainloop()

