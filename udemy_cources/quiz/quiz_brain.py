class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        users_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(users_answer, current_question.answer)

    def check_answer(self, users_answer, current_answer):
        if users_answer.lower() == current_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That`s the wrong answer!")
        print(f"The correct answer was: {current_answer}")
        print(f"The current score is: ({self.score}/{self.question_number})\n")


class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
