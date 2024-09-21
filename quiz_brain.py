from html import unescape

class QuizBrain:
    """
    This script stores the logic of the quiz
    """
    def __init__(self, q_list):
        self.current_question = None
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
        self.current_question = self.question_list[self.question_number]
        # Once the question is selected, we increase the question number to fix wrong number shown. (example, question 0 should show 1 to user)
        self.question_number += 1
        # Unescape HTML Entities in question
        question = unescape(self.current_question.text)

        return question

    def check_answer(self, user_answer):
        """
        Checks if user's answer is correct
        :param user_answer: User's answer
        """
        # If it's correct, the user scores a point
        if user_answer == self.current_question.answer:
            self.score += 1
            return True
        else:
            return False