from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class Interface:
    def __init__(self,quiz:QuizBrain):
        self.question=quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.canvas = Canvas(height=250, width=300)
        self.question_text=self.canvas.create_text(125, 150,fill=THEME_COLOR,width=260, text="Question goes here", font=("Arial", 15, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2,pady=50)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white",font=("Arial", 12, "bold"))
        self.score.grid(row=0, column=1)
        right = PhotoImage(file="./images/true.png")
        wrong = PhotoImage(file="./images/false.png")
        self.correct = Button(image=right, height=100, width=100, highlightthickness=0,command=self.ans_true)
        self.incorrect = Button(image=wrong, height=100, width=100, highlightthickness=0,command=self.ans_false)
        self.correct.grid(row=2, column=0)
        self.incorrect.grid(row=2, column=1)
        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.question.still_has_questions():
            self.score.config(text=f"Score: {self.question.score}")
            q_text=self.question.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You have reached the end of the quiz")
            self.correct.config(state="disabled")
            self.incorrect.config(state="disabled")

    def ans_true(self):
        is_right=self.question.check_answer("True")
        self.feedback(is_right)
    def ans_false(self):
        is_right=self.question.check_answer("False")
        self.feedback(is_right)

    def feedback(self,ans):
        if ans:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        # self.window.after_cancel()
        self.window.after(1000, func=self.next_question)

