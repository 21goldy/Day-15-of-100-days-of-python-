from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizly")
        self.window.config(padx=20, pady=20)

        # canvas setup and screen
        self.canvas = Canvas(width=800, height=550)
        self.card = PhotoImage(file="images/card_back.png")
        self.canvas.create_image(400, 268, image=self.card)
        self.score_board = self.canvas.create_text(120, 60, text=f"Score: {0}", font=("Courier", 20, "bold"),
                                                   fill="white")
        self.question_text = self.question_text = self.canvas.create_text(
            400,
            268,
            width=780,
            text="Question",
            font=("Courier", 30, "bold"),
            fill="white"
        )
        self.canvas.grid(row=0, column=0, columnspan=2)

        # false button
        self.false = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false, highlightthickness=0, command=self.user_false)
        self.false_button.grid(row=1, column=0)

        # true button
        self.true = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true, highlightthickness=0, command=self.user_true)
        self.true_button.grid(row=1, column=1)
        self.get_another_question()

        self.window.mainloop()

    def get_another_question(self):
        self.canvas.itemconfig(self.question_text, fill="white")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.score_board, text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end!", fill="white")
            self.canvas.itemconfig(self.score_board, text=f"Score: {self.quiz.score}", fill="white")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def user_true(self):
        self.feedback(self.quiz.check_answer("True"))

    def user_false(self):
        is_right = self.quiz.check_answer("False")
        self.feedback(is_right)

    def feedback(self, is_right):
        if is_right:
            self.canvas.itemconfig(self.question_text, fill="green")
        else:
            self.canvas.itemconfig(self.question_text, fill="red")
        self.window.after(1000, self.get_another_question)
