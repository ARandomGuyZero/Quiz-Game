from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    """
    This script has the logic of the quiz interface
    """
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

    def get_next_question(self):
        """
        Gets the quiz question text and sets it to the label
        :return:
        """
        self.canvas.config(bg="white")
        # Check if we still have questions
        if self.quiz.still_has_questions():
            # Update the score
            self.score_label.config(text=f"Score: {self.quiz.score}")
            # Get the next question
            question_text = self.quiz.next_question()
            # Update the label to get next question
            self.canvas.itemconfig(self.question_label, text=question_text)
        else:
            # Set message at the end of the quiz.
            self.canvas.itemconfig(self.question_label, text="You've reached the end of the quiz.")
            # Disable the buttons
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def is_true_pressed(self):
        """
        Checks the answer and gets feedback
        :return:
        """
        self.give_feedback(self.quiz.check_answer(user_answer="True"))

    def is_false_pressed(self):
        """
        Checks the answer and gets feedback
        :return:
        """
        self.give_feedback(self.quiz.check_answer(user_answer="False"))

    def give_feedback(self, is_right):
        # If it's right, the canvas is temporarily of a color to give feedback
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        # Update the canvas for the next question
        self.window.after(1000, self.get_next_question)
