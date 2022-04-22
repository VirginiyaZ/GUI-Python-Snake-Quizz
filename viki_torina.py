
# Simple Viktorina using Tkinter (by Virginiya Zubar )
 

from tkinter import *
from tkinter import messagebox as mb
import json



# create class to define the components of the GUI 
class Viktorina:
    
    def __init__(self):
# set question number to 0     
        self.question_number=0 
         
# assigns functions 
        self.display_title()
        self.display_question()
         
# Option in opt_selected holds an integer value which is used for
        self.opt_selected=IntVar()
         
# Radio buttons for the current question 
        self.opts=self.radio_buttons()
         
# Options for the current question
        self.display_options()
         
# Buttons Next and Exit
        self.buttons()
         
# Number of questions
        self.data_size=len(question)
         
# Counter of correct answers
        self.correct=0
 
 
# Methods to display the result, count answers, and message box to show info
    def display_result(self):
         
        # calculates the wrong count
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
         
        # calcultaes the percentage of correct answers
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
         
        # Shows a message box to display the result
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")
 
 
   
    def check_ans(self, question_number):
         
        # checks for if the selected option is correct
        if self.opt_selected.get() == answer[question_number]:
            return True
 
    
    def next_btn(self):
         
        # Check if the answer is correct
        if self.check_ans(self.question_number):
             
            self.correct += 1
         
        self.question_number += 1
        
        if self.question_number==self.data_size:
             
            # if it is correct then it displays the score
            self.display_result()
             
            # destroys the GUI App
            win.destroy()
        else:
            # shows the next question
            self.display_question()
            self.display_options()
 
 
    def buttons(self):
         
        # The first button is the Next button to move to the next question
        next_button = Button(win, text="Next",command=self.next_btn,
        width=10,bg="#D8CED8",fg="#595D50",font=("Ariel",14,"bold"))
        next_button.place(x=80,y=340)
         
        # This is the second button which is used to Quit the GUI App
        quit_button = Button(win, text="Quit", command=win.destroy,
        width=5,bg="#BC99E2", fg="#595D50",font=("Ariel",14," bold"))
        quit_button.place(x=360,y=340)
 
 
    def display_options(self):
        val=0
         
        # deselecting the options
        self.opt_selected.set(0)
         
        # looping over the options to be displayed 
        for option in options[self.question_number]:
            self.opts[val]['text']=option
            val+=1
 
 
    
    def display_question(self):
        # setting the Question properties
        question_number = Label(win, text=question[self.question_number], width=45,
        font=( 'Ariel' ,14, 'bold' ), anchor= 'sw' )
        question_number.place(x=50, y=80)
 
 
    # Display Title
    def display_title(self):
        # The title to be shown
        title = Label(win, text="Viktorina",
        width=27, bg="#CA7CCB",fg="black", font=("Ariel", 20, "bold"))
        title.place(x=9, y=5)
 
 
    def radio_buttons(self):
        qusn_list = [] # create a list with an empty list of options
        pos_y = 150 # position of the first option
         
        # adding the options to the list
        while len(qusn_list) < 4:
             
            # setting the radio button properties
            radio_btn = Radiobutton(win,text=" ",variable=self.opt_selected,
            value = len(qusn_list)+1,font = ("Ariel",14))
            qusn_list.append(radio_btn)
            radio_btn.place(x = 80, y = pos_y)
            pos_y += 35
         
        return qusn_list
 
# Create a GUI Window
win = Tk()
 
# set the size of the GUI Window
w = win.winfo_screenwidth()
h = win.winfo_screenheight()
w=w//2
h=h//2
w=w-200
h=h-200
win.geometry(f'500x400+{w}+{h}')
 
# set the title of the Window
win.title("Viktorina")
 
# get the data from the json file
with open('data.json') as f:
    data = json.load(f)
 
# set the question, options, and answer
question = (data['question'])
options = (data['options'])
answer = (data[ 'answer'])
 

quiz = Viktorina()

win.mainloop()
 
