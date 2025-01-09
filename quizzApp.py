import tkinter

class QuizApp:
    def __init__(self):
        # Window setup
        self.root = tkinter.Tk()
        self.root.title("QUIZ")
        self.root.geometry('1000x600')  # Increased window size for better spacing
        self.score = 0
        
        # Initial widgets
        self.label_title = tkinter.Label(self.root, text="QUIZ", font=("arial", 50))
        self.label_title.place(x=400, y=50)  # Centered the title
        
        self.label_username = tkinter.Label(self.root, text="Username", font=("arial", 30))
        self.label_username.place(x=250, y=250)
        
        self.entry_username = tkinter.Entry(self.root, font=("arial", 30))
        self.entry_username.place(x=450, y=250)
        
        self.start_button = tkinter.Button(self.root, text="ENTER", font=("arial", 30), command=self.question1)
        self.start_button.place(x=400, y=350)
        
        # Store current widgets for cleanup
        self.current_widgets = []

    def clear_screen(self):
        """Clear all current widgets from the screen"""
        for widget in self.current_widgets:
            widget.destroy()
        self.current_widgets.clear()

    def increase_score(self):
        self.score += 1

    def question1(self):
        self.clear_screen()
        
        label_q = tkinter.Label(self.root, text="Question 1", font=("Arial", 35))
        label_q.place(x=400, y=50)
        
        label = tkinter.Label(self.root, text="Which of them is a Keyword in Python?", font=("Arial", 30))
        label.place(x=200, y=150)
        
        # Create a frame for buttons
        button_frame = tkinter.Frame(self.root)
        button_frame.place(x=200, y=250)
        
        op1 = tkinter.Button(button_frame, text="range", font=("Arial", 20), width=10, command=self.question2)
        op1.grid(row=0, column=0, padx=20, pady=10)
        
        op2 = tkinter.Button(button_frame, text="def", font=("Arial", 20), width=10,
                           command=lambda: [self.increase_score(), self.question2()])
        op2.grid(row=0, column=1, padx=20, pady=10)
        
        op3 = tkinter.Button(button_frame, text="Val", font=("Arial", 20), width=10, command=self.question2)
        op3.grid(row=1, column=0, padx=20, pady=10)
        
        op4 = tkinter.Button(button_frame, text="to", font=("Arial", 20), width=10, command=self.question2)
        op4.grid(row=1, column=1, padx=20, pady=10)
        
        self.current_widgets.extend([label_q, label, button_frame])

    def question2(self):
        self.clear_screen()
        
        label_q = tkinter.Label(self.root, text="Question 2", font=("Arial", 35))
        label_q.place(x=400, y=50)
        
        label = tkinter.Label(self.root, text="Which of the following is built-in function in Python?", font=("Arial", 30))
        label.place(x=200, y=150)
        
        button_frame = tkinter.Frame(self.root)
        button_frame.place(x=200, y=250)
        
        op1 = tkinter.Button(button_frame, text="factorial()", font=("Arial", 20), width=10, command=self.question3)
        op1.grid(row=0, column=0, padx=20, pady=10)
        
        op2 = tkinter.Button(button_frame, text="print()", font=("Arial", 20), width=10,
                           command=lambda: [self.increase_score(), self.question3()])
        op2.grid(row=0, column=1, padx=20, pady=10)
        
        op3 = tkinter.Button(button_frame, text="seed()", font=("Arial", 20), width=10, command=self.question3)
        op3.grid(row=1, column=0, padx=20, pady=10)
        
        op4 = tkinter.Button(button_frame, text="sqrt()", font=("Arial", 20), width=10, command=self.question3)
        op4.grid(row=1, column=1, padx=20, pady=10)
        
        self.current_widgets.extend([label_q, label, button_frame])

    def question3(self):
        self.clear_screen()
        
        label_q = tkinter.Label(self.root, text="Question 3", font=("Arial", 35))
        label_q.place(x=400, y=50)
        
        label = tkinter.Label(self.root, text="Which of the following is not the core datatype in Python?", font=("Arial", 30))
        label.place(x=150, y=150)
        
        button_frame = tkinter.Frame(self.root)
        button_frame.place(x=200, y=250)
        
        op1 = tkinter.Button(button_frame, text="Tuple", font=("Arial", 20), width=10, command=self.question4)
        op1.grid(row=0, column=0, padx=20, pady=10)
        
        op2 = tkinter.Button(button_frame, text="Dictionary", font=("Arial", 20), width=10, command=self.question4)
        op2.grid(row=0, column=1, padx=20, pady=10)
        
        op3 = tkinter.Button(button_frame, text="Lists", font=("Arial", 20), width=10, command=self.question4)
        op3.grid(row=1, column=0, padx=20, pady=10)
        
        op4 = tkinter.Button(button_frame, text="Class", font=("Arial", 20), width=10,
                           command=lambda: [self.increase_score(), self.question4()])
        op4.grid(row=1, column=1, padx=20, pady=10)
        
        self.current_widgets.extend([label_q, label, button_frame])

    def question4(self):
        self.clear_screen()
        
        label_q = tkinter.Label(self.root, text="Question 4", font=("Arial", 35))
        label_q.place(x=400, y=50)
        
        label = tkinter.Label(self.root, text="Who developed python programming language?", font=("Arial", 30))
        label.place(x=150, y=150)
        
        button_frame = tkinter.Frame(self.root)
        button_frame.place(x=200, y=250)
        
        op1 = tkinter.Button(button_frame, text="Wick Van Rossum", font=("Arial", 20), width=15, command=self.question5)
        op1.grid(row=0, column=0, padx=20, pady=10)
        
        op2 = tkinter.Button(button_frame, text="Rasmus Lerdorf", font=("Arial", 20), width=15, command=self.question5)
        op2.grid(row=0, column=1, padx=20, pady=10)
        
        op3 = tkinter.Button(button_frame, text="Guido Van Rossum", font=("Arial", 20), width=15,
                           command=lambda: [self.increase_score(), self.question5()])
        op3.grid(row=1, column=0, padx=20, pady=10)
        
        op4 = tkinter.Button(button_frame, text="Niene Stom", font=("Arial", 20), width=15, command=self.question5)
        op4.grid(row=1, column=1, padx=20, pady=10)
        
        self.current_widgets.extend([label_q, label, button_frame])

    def question5(self):
        self.clear_screen()
        
        label_q = tkinter.Label(self.root, text="Question 5", font=("Arial", 35))
        label_q.place(x=400, y=50)
        
        label = tkinter.Label(self.root, text="Which of the following is the extension for Python File?", font=("Arial", 30))
        label.place(x=150, y=150)
        
        button_frame = tkinter.Frame(self.root)
        button_frame.place(x=200, y=250)
        
        op1 = tkinter.Button(button_frame, text=".python", font=("Arial", 20), width=10, command=self.show_score)
        op1.grid(row=0, column=0, padx=20, pady=10)
        
        op2 = tkinter.Button(button_frame, text=".p", font=("Arial", 20), width=10, command=self.show_score)
        op2.grid(row=0, column=1, padx=20, pady=10)
        
        op3 = tkinter.Button(button_frame, text=".pl", font=("Arial", 20), width=10, command=self.show_score)
        op3.grid(row=1, column=0, padx=20, pady=10)
        
        op4 = tkinter.Button(button_frame, text=".py", font=("Arial", 20), width=10,
                           command=lambda: [self.increase_score(), self.show_score()])
        op4.grid(row=1, column=1, padx=20, pady=10)
        
        self.current_widgets.extend([label_q, label, button_frame])

    def save_score(self):
        """Save the username and score to a file"""
        username = self.entry_username.get()
        with open("scores.txt", "a") as file:
            file.write(f"{username}: {self.score}/5\n")

    def show_score(self):
        self.clear_screen()
        
        # Score title at the top
        label_score_title = tkinter.Label(self.root, text="SCORE", font=("Arial", 48))
        label_score_title.place(x=400, y=50)
        
        # Create a frame for score information
        score_frame = tkinter.Frame(self.root)
        score_frame.place(x=200, y=200)
        
        # Username display
        username = self.entry_username.get()
        label_name = tkinter.Label(score_frame, text="Username:", font=("Arial", 35))
        label_name.pack(pady=20)
        
        label_name_value = tkinter.Label(score_frame, text=username, font=("Arial", 35))
        label_name_value.pack(pady=20)
        
        # Score display
        label_final_score = tkinter.Label(score_frame, 
                                        text=f"Your Score: {self.score}/5", 
                                        font=("Arial", 40))
        label_final_score.pack(pady=40)
        
        # Add a play again button
        play_again_btn = tkinter.Button(score_frame, 
                                      text="Play Again", 
                                      font=("Arial", 20),
                                      command=self.restart_quiz)
        play_again_btn.pack(pady=30)
        
        self.current_widgets.extend([label_score_title, score_frame])
        self.save_score()

    def restart_quiz(self):
        # Reset score
        self.score = 0
        # Clear screen
        self.clear_screen()
        # Reset to initial state
        self.__init__()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    quiz = QuizApp()
    quiz.run()
