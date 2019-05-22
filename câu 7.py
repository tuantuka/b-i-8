import tkinter
import random

colours = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0

timeleft = 30

def startGame(event):
    if timeleft == 30:
        countdown()
    nextColour()

def nextColour():
    global score
    global timeleft
    if timeleft > 0:
        e.focus_set()
        if e.get().lower() == colours[1].lower():
            score += 1
        e.delete(0, tkinter.END)
        random.shuffle(colours)

        label.config(fg = str(colours[1]), text = str(colours[0]))
        scorelabel.config(text = "Score: " + str(score))

def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timelabel.config(text = "Time left: " + str(timeleft))
        timelabel.after(1000, countdown)

root = tkinter.Tk()
root.title("COLORGAME")
root.geometry("375x200")

instructions = tkinter.Label(root, text = "Type in the colour of the words, and not the word text!", font = ('Times', 12))
instructions.pack()

scoreLabel = tkinter.Label(root, text = "Press enter to start", font = ('Times', 12))
scoreLabel.pack()

timeLabel = tkinter.Label(root, text = "Time left: " + str(timeleft), font = ('Times', 12))
timeLabel.pack()

label = tkinter.Label(root, font = ('Times', 12))
label.pack()

e = tkinter.Entry(root)
e.pack()

root.mainloop()