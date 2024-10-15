import tkinter
from tkinter import *
import pandas as pd
import random

to_learn={}
current_card={}

# Convert Dataframe to dictionary
try:
    df= pd.read_csv("data/to_learn.csv")

except FileNotFoundError:
    df= pd.read_csv("data/to_learn")

else:
    to_learn= df.to_dict(orient="records")

#Create a method which takes a french word as a key from dictionary of words.

def words_run():
    global current_card
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word,text=current_card["French Word"])
    window.after(3000,flip_card)

#
def flip_card():
    canvas.itemconfig(card_title,text="English")
    canvas.itemconfig(card_word, text=current_card["English Translation"])
#remove the already known words from the dictionary of words
def known_words():
    to_learn.remove(current_card)
    remaining_words=pd.DataFrame(to_learn)
    remaining_words.to_csv("data/to_learn.csv", index=False )
    words_run()



BG="#B1DDC6"
window=Tk()
window.title("Flash Card")
window.config(padx=50,pady=50, bg=BG)
window.after(3000, flip_card)


canvas=Canvas(width=800,height=526,highlightthickness=0)
card_title=canvas.create_text(400,150, text="French",font=("Ariel",20,"italic"))
card_word = canvas.create_text(400,263, text="Word",font=("Ariel",40,"italic"))
canvas.grid(row=0, column=0, columnspan=2)

unknown_img=PhotoImage(file="images/wrong.png")
cross_button=tkinter.Button(image=unknown_img,command=words_run)
cross_button.grid(row=1,column=0)

known_img=PhotoImage(file="images/right.png")
tick_button=tkinter.Button(image=known_img,command=known_words)
tick_button.grid(row=1,column=1)

words_run()
window.mainloop()