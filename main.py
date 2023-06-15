from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# put the questions and the answers from the request in a list
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# pass the questions to the quiz
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
