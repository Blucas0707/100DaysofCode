from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    text = question["text"]
    answer = question["answer"]
    new_q = Question(text,answer)
    question_bank.append(new_q)


game = QuizBrain(question_bank)
while game.still_has_question():
    game.next_question()
game.complete_quiz()