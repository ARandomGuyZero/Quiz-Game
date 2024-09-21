from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, font=("Arial", 10), fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_label = self.canvas.create_text(150, 125, width=250, text="Some question text.", font=("Arial", 15, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_img, command=self.is_true_pressed, highlightthickness=0)
        self.true_btn.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_img, command=self.is_false_pressed, highlightthickness=0)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def is_true_pressed(self):
        self.quiz.check_answer(user_answer="True")
        self.get_next_question()

    def is_false_pressed(self):
        self.quiz.check_answer(user_answer="False")
        self.get_next_question()

    def get_next_question(self):
        """
        Gets the quiz question text and sets it to the label
        :return:
        """
        question_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_label, text=question_text)