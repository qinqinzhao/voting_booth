from tkinter import *

top = Tk()

frame1 = Frame(top)
frame2 = Frame(top)

batman_score = 0
superman_score = 0
spiderman_score = 0
wonder_woman_score = 0

winner_label = Label(frame2, text="Tied", width=14)

def set_winner(name, score):
    global frame2
    max_score = -1
    max_num = -1
    for x in [batman_score, superman_score, spiderman_score, wonder_woman_score]:
        if x > max_score:
            max_score = x
            max_num = 1
        elif x == max_score:
            max_num += 1
    if score == max_score:
        if max_num == 1:
            winner_label["text"] = name
        else:
            winner_label["text"] = "Tied"

def batman_score_handler():
    global batman_score, frame2
    batman_score += 1
    Label(frame2, text=str(batman_score)).grid(row=1, column=1)
    set_winner("Batman", batman_score)

def superman_score_handler():
    global superman_score, frame2
    superman_score += 1
    Label(frame2, text=str(superman_score)).grid(row=2, column=1)
    set_winner("Superman", superman_score)

def spiderman_score_handler():
    global spiderman_score, frame2
    spiderman_score += 1
    Label(frame2, text=str(spiderman_score)).grid(row=3, column=1)
    set_winner("Spiderman", spiderman_score)

def wonder_woman_score_handler():
    global wonder_woman_score, frame2
    wonder_woman_score += 1
    Label(frame2, text=str(wonder_woman_score)).grid(row=4, column=1)
    set_winner("Wonder Woman", wonder_woman_score)

frame1.pack(side='top')
frame2.pack(side='top')

Label(frame1, text="Vote for your favorite superhero!", bg='white').pack()

Label(frame2, text="SUPERHERO").grid(row=0, column=0)
Button(frame2, text="Batman", command=batman_score_handler, bg='black', fg='white').grid(row=1, column=0, sticky=W+E)
Button(frame2, text="Superman", command=superman_score_handler, bg='blue', fg='white').grid(row=2, column=0, sticky=W+E)
Button(frame2, text="Spiderman", command=spiderman_score_handler, bg='red', fg='black').grid(row=3, column=0, sticky=W+E)
Button(frame2, text="Wonder Woman", command=wonder_woman_score_handler, bg='yellow', fg='black').grid(row=4, column=0, sticky=W+E)
Label(frame2, text="Winner so far").grid(row=5, column=0)

Label(frame2, text="VOTES").grid(row=0, column=1, sticky=W+E)
Label(frame2, text="0").grid(row=1, column=1, sticky=W+E)
Label(frame2, text="0").grid(row=2, column=1, sticky=W+E)
Label(frame2, text="0").grid(row=3, column=1, sticky=W+E)
Label(frame2, text="0").grid(row=4, column=1, sticky=W+E)
winner_label.grid(row=5, column=1)

mainloop()
