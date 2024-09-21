from html import unescape

class QuizBrain:
    """
    This script stores the logic of the quiz
    """
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        """
        Check if the list still has questions
        :return: True if current question number has reached question list limit, else False
        """
        if not self.question_number == len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        """
        Simple logic to print question for user to answer
        """
        # Selects the next question using sef.question_number for index
        current_question = self.question_list[self.question_number]
        # Once the question is selected, we increase the question number to fix wrong number shown. (example, question 0 should show 1 to user)
        self.question_number += 1
        # Unescape HTML Entities in question
        question = unescape(current_question.text)
        # User answers the question
        user_answer = input(f"Q.{self.question_number}: {question} (True/False)\n").capitalize()
        # Check if the answer is correct
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """
        Checks if user's answer is correct
        :param user_answer: User's answer
        :param correct_answer: The question's correct answer
        """
        # If it's correct, the user scores a point
        if user_answer == correct_answer:
            self.score += 1
            print("You got it right!")
        else:
            print("Whoops! You got it wrong!")
        # Print correct answer and current score
        print(f"The correct answer was {correct_answer}")
        print(f"Your score is {self.score}/{self.question_number}.")
        print("\n")
