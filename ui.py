from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
TRUE_IMG_PATH = "images/true.png"
FALSE_IMG_PATH = "images/false.png"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # window
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=40, pady=40, bg=THEME_COLOR)
        # images
        self.true_img = PhotoImage(file=TRUE_IMG_PATH)
        self.false_img = PhotoImage(file=FALSE_IMG_PATH)
        # score label
        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}", fg="white",font=("Arial", 20, "bold"))
        self.score_label.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0, sticky="nsew")
        # canvas
        self.canvas = Canvas()
        self.canvas.config(width=600, height=500)
        self.question_text = self.canvas.create_text(300, 250,
                                                     width=560,
                                                     text="sample text for the questions!",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(columnspan=2, column=0, row=1, pady=50)
        # buttons
        self.true_btn = Button(image=self.true_img, highlightthickness=0, command=self.true_pressed)
        self.true_btn.grid(column=0, row=2)
        self.false_btn = Button(image=self.false_img, highlightthickness=0, command=self.false_pressed)
        self.false_btn.grid(column=1, row=2)
        # first question
        self.get_next_question()
        # main loop
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've complete the quiz")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_pressed(self):
       is_right = self.quiz.check_answer("True")
       self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
