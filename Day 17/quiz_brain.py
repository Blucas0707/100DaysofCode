#TODO 1: asking the questions
#TODO 2: checking if the answer is right
#TODO 3: checking ig we're the end of the quiz

class QuizBrain:
    def __init__(self, question):
        self.question_num = 0
        self.question_list = question
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_num]
        self.question_num += 1
        ans = input(f"Q.{self.question_num}: {current_question.text} (True/False)?:")
        self.check_answer(ans, current_question.answer)

    def still_has_question(self):
        return self.question_num < len(self.question_list)

    def check_answer(self,ans, correct_ans):
        if ans.lower() == correct_ans.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong!")
        print(f"The correct answer was {correct_ans}.")
        print(f"Your current score is: {self.score}/{self.question_num}.")
        print("\n")

    def complete_quiz(self):
        print("You've completed the quiz.")
        print(f"Your final score is {self.score}/{self.question_num}.")