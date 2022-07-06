from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

"""TODO: write a for loop to iterate over he question_data"""
""" create a question object from each entry """
"""append each new question in the question bank"""

question_bank = []
for question in question_data:
    question_text = question["question"]  # extract with the key in question_data
    question_answer = question["correct_answer"]
    new_q = Question(question_text, question_answer)
    question_bank.append(new_q)


quiz = QuizBrain(question_bank)


while quiz.still_has_questions:
    quiz.next_question()

print("Congrats! You've completed the quiz! 🌟")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

