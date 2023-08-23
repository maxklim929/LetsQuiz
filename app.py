from tkinter import *
from tkmacosx import Button
import random
import sys

main = Tk()
main.title('QuizFree')
screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()
main.geometry("{}x{}".format(screen_width,  screen_height))
main["bg"] = "#0A092B"

qa = {}
track_score = {}


# Finds the text file named "terms.txt" and splits
# into a map of questions and answers using a map
def read_file(line_arr):
    switch = 0
    term = "empty"
    for line in line_arr:
        if switch == 0:
            term = line[:-1]
            switch = 1
        else:
            qa[line[:-1]] = term
            track_score[line[:-1]] = 0
            switch = 0


# GUI and logic for developing a multiple choice question
def multiple(t1, t2, t3, t4, question, answer, ind):
    main.C = Canvas(main, width=1400, height=1000, bg="#0A092B", highlightthickness=0)
    main.C.pack()
    main.C.create_rectangle(10, 20, 1400, 850, fill='#303854', outline="#303854")
    # Continuing on to the next question
    def cont(): 
        for child in main.winfo_children():
            child.destroy()
        create_Quest()

    # Shows the window for answering the question correctly
    def correct():
        c = Label(main,text="Correct", fg="white", bg="#303854", font="Arial 20 bold")
        c.place(relx=0.5, rely=0.35, anchor=CENTER)
        track_score[question] += 1
        forward = Button(main, text="Continue?", width=400, height=100, bg="#303854", fg="white", font="Arial 17 bold", command=cont).place(relx=0.5, rely=0.85, anchor=CENTER)

    # Shows the window for answering a question incorrectly
    def incorr():
        c = Label(main,text="Incorrect: " + answer, fg="white", bg="#303854", font="Arial 20 bold", wraplength=main.winfo_width() + 200)
        c.place(relx=0.5, rely=0.35, anchor=CENTER)
        track_score[question] -= 1
        forward = Button(main, text="Continue?", width=400, height=100, bg="#303854", fg="white", font="Arial 17 bold", command=cont).place(relx=0.5, rely=0.85, anchor=CENTER)
    
    # Logic for what place in the multiple choice to place the correct answer
    l = Label(main,text=question,font="Arial 22 bold", bg="#303854", wraplength=1000)
    l.place(relx=0.5, rely=0.13, anchor=CENTER)
    # GUI placement of correct answer
    if ind == 0:
        c1 = Button(main, text=t1, width=600, height=100, bg="#303854", fg="white", font="Arial 20 bold", command=correct).place(relx=0.3, rely=0.5, anchor=CENTER)
        c2 = Button(main, text=t2, width=600, height=100, bg="#303854", fg="white", font="Arial 20 bold", command=incorr).place(relx=0.7, rely=0.5, anchor=CENTER)
        c3 = Button(main, text=t3, width=600, height=100, bg="#303854", fg="white", font="Arial 20 bold", command=incorr).place(relx=0.3, rely=0.7, anchor=CENTER)
        c4 = Button(main, text=t4, width=600, height=100, bg="#303854", fg="white", font="Arial 20 bold", command=incorr).place(relx=0.7, rely=0.7, anchor=CENTER)
    if ind == 1:
        c1 = Button(main, text=t1, width=600, height=100, bg="#303854", fg="white", font="Arial 20 bold", command=incorr).place(relx=0.3, rely=0.5, anchor=CENTER)
        c2 = Button(main, text=t2, width=600, height=100, bg="#303854", fg="white", font="Arial 20 bold", command=correct).place(relx=0.7, rely=0.5, anchor=CENTER)
        c3 = Button(main, text=t3, width=600, height=100, bg="#303854", fg="white", font="Arial 20 bold", command=incorr).place(relx=0.3, rely=0.7, anchor=CENTER)
        c4 = Button(main, text=t4, width=600, height=100, bg="#303854", fg="white", font="Arial 20 bold", command=incorr).place(relx=0.7, rely=0.7, anchor=CENTER)
    if ind == 2:
        c1 = Button(main, text=t1, width=600, height=100, bg="#303854", fg="white", font="Arial 20 bold", command=incorr,).place(relx=0.3, rely=0.5, anchor=CENTER)
        c2 = Button(main, text=t2, width=600, height=100, bg="#303854", fg="white", font="Arial 20 bold", command=incorr).place(relx=0.7, rely=0.5, anchor=CENTER)
        c3 = Button(main, text=t3, width=600, height=100, bg="#303854", fg="white", font="Arial 20 bold", command=correct).place(relx=0.3, rely=0.7, anchor=CENTER)
        c4 = Button(main, text=t4, width=600, height=100, bg="#303854", fg="white", font="Arial 20 bold", command=incorr).place(relx=0.7, rely=0.7, anchor=CENTER)
    if ind == 3:
        c1 = Button(main, text=t1, width=600, height=100, bg="#303854", fg="white", font="Arial 20 bold", command=incorr,).place(relx=0.3, rely=0.5, anchor=CENTER)
        c2 = Button(main, text=t2, width=600, height=100, bg="#303854", fg="white", font="Arial 20 bold", command=incorr).place(relx=0.7, rely=0.5, anchor=CENTER)
        c3 = Button(main, text=t3, width=600, height=100, bg="#303854", fg="white", font="Arial 20 bold", command=incorr).place(relx=0.3, rely=0.7, anchor=CENTER)
        c4 = Button(main, text=t4, width=600, height=100, bg="#303854", fg="white", font="Arial 20 bold", command=correct).place(relx=0.7, rely=0.7, anchor=CENTER)

# GUI and logic for developing a short-answer question
def text(question, answer):
    main.C = Canvas(main, width=1400, height=1000, bg="#0A092B", highlightthickness=0)
    main.C.pack()
    main.C.create_rectangle(10, 20, 1400, 850, fill='#303854', outline="#303854")
    def cont(): 
        for child in main.winfo_children():
            child.destroy()
        create_Quest()

    s1_var = StringVar()
    # Shows the window for answering the question correctly
    def correct():
        c = Label(main,text="Correct", fg="white", font="Arial 20 bold", bg="#303854", wraplength=main.winfo_width())
        c.place(relx=0.5, rely=0.35, anchor=CENTER)
        track_score[question] += 1
        forward = Button(main, text="Continue?", width=400, height=100, bg="#303854", fg="white", font="Arial 17 bold", command=cont).place(relx=0.5, rely=0.85, anchor=CENTER)

    # Shows the window for answering the question incorrectly
    def incorr():
        c = Label(main,text="Incorrect: " + answer, fg="white", bg="#303854", font="Arial 17 bold", wraplength=main.winfo_width() + 200)
        c.place(relx=0.5, rely=0.35, anchor=CENTER)
        track_score[question] -= 1
        forward = Button(main, text="Continue?", width=400, height=100, bg="#303854", fg="white", font="Arial 17 bold", command=cont).place(relx=0.5, rely=0.85, anchor=CENTER)

    def buttonClick():
        opt = s1_var.get()
        if opt == answer:
            correct()
        else:
            incorr()
    e1 = Entry(main, textvariable= s1_var, width=80, font="Arial 25 bold")
    e1.place(relx=0.5, rely=0.5, anchor=CENTER)
    s1 = Button(main, text="Submit", width=400, height=100, command=buttonClick).place(relx=0.5, rely=0.75, anchor=CENTER)
    l = Label(main,text=question,font="Arial 25 bold", bg="#303854", wraplength=1000)
    l.place(relx=0.5, rely=0.13, anchor=CENTER)

def create_opt(answer, values, choices):
    choice = random.choice(values)
    if answer is not choice and choice not in choices and len(choice) != 0:
        return choice
    else:
        while len(choice) == 0 or answer is choice or choice in choices:
            choice = random.choice(values)
        return choice

def create_Quest():
    quests = list(qa.keys())
    ans = list(qa.values())
    
    num_finished = 0
    for val in list(track_score.values()): #Tracks if finished or not
        if val == 5:
            num_finished += 1

    if num_finished == len(list(track_score.values())):
        finished()

    choice = random.choice(quests)
    while track_score[choice] >= 3:
        choice = random.choice(quests)
  
    choices = []
    if track_score[choice] <= 3:
        answer = qa[choice]
        t1 = create_opt(answer, ans, choices)
        choices.append(t1)
        t2 = create_opt(answer, ans, choices)
        choices.append(t2)
        t3 = create_opt(answer, ans, choices)
        choices.append(t3)
        t4 = create_opt(answer, ans, choices)
        pick = random.randrange(4)
        if pick == 0:
            multiple(answer, t2, t3, t4, choice, answer, 0)
        if pick == 1:
            multiple(t1, answer, t3, t4, choice, answer, 1)
        if pick == 2:
            multiple(t1, t2, answer, t4, choice, answer, 2)
        if pick == 3:
            multiple(t1, t2, t3, answer, choice, answer, 3)
    elif track_score[choice] >= 1:
        text(choice, qa[choice])
    else:
        create_Quest()

def finished():
    for child in main.winfo_children():
        child.destroy()



f = open('terms.txt','r')
read_file(f.readlines())
create_Quest()
main.mainloop()