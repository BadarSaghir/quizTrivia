from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
from tkinter import *


class QuizUI:
    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="White")
        self.question_text = self.canvas.create_text(150, 125, width=280,
                                                     text="Some quesion text", fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=3, pady=20, padx=10)
        true_img = PhotoImage(file="./images/true.png")
        false_img = PhotoImage(file="./images/false.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_press)
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_press)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            q_text = f"You've completed the quiz\n Your final score was: {self.quiz.score}/{len(self.quiz.question_list)}"
            self.canvas.itemconfig(self.question_text, text=q_text)

    def true_press(self):
        is_right=self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def false_press(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right:bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
        # self.canvas.config(bg="white")


        pass
