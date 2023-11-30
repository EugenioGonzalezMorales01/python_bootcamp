from tkinter import *
from pandas import *
from random import *

BACKGROUND_COLOR = "#B1DDC6"

data = None
words = None
fr_word = None
en_word = None
wrong_en_word = None
right_en_word = None
turned_card = False

score = 0


def open_csv():
    global data
    global words

    try:
        with open("data/words_to_learn.csv") as file:
            data = read_csv(file)
            print("WTL")
    except FileNotFoundError:
        with open("data/french_words.csv") as file:
            data = read_csv(file)
            print("FW")
    finally:
        words = data.iloc[randint(0, len(data))]
        file.close()


def get_words():
    global words
    global fr_word
    global wrong_en_word
    global right_en_word

    fr_word = words["French"]
    right_en_word = words["English"]
    wrong_en_word = right_en_word
    while right_en_word == wrong_en_word:
        wrong_en_word = data.iloc[randint(0, len(data))]["English"]
    print(f" {fr_word} == {right_en_word}")


def turn_card():
    global turned_card
    global f_c_img
    global b_c_img

    print("Clicked")
    if turned_card:
        lan_lab.config(text="French", fg="black", background="white")
        word_lab.config(text=fr_word, fg="black", background="white")
        turned_card = False
        print(f"Carta volteada al frente {turned_card}")
        card_button.config(image=f_c_img)
    else:
        lan_lab.config(text="English", fg="white", background=BACKGROUND_COLOR)
        word_lab.config(text=en_word, fg="white", background=BACKGROUND_COLOR)
        turned_card = True
        print(f"Carta volteada atras {turned_card}")
        card_button.config(image=b_c_img)


def get_en_word():
    global en_word
    global right_en_word
    global wrong_en_word

    ran = randint(0, 1)
    if ran == 0:
        en_word = right_en_word
    else:
        en_word = wrong_en_word
    return en_word


def save_progres():
    global data
    row_num = data[data["French"] == fr_word].index
    data = data.drop(row_num, axis=0)
    with open("data/words_to_learn.csv", "w") as file:
        file.write(data.to_csv(index=False))
    file.close()


def reset_card():
    global turned_card

    turned_card = True
    open_csv()
    get_words()
    get_en_word()
    turn_card()
    win.title(f"Flashy - Score: {score}")


def right_button():
    global score

    if en_word == right_en_word:
        score += 1
        save_progres()
    else:
        score -= 1

    reset_card()


def wrong_button():
    global score

    if en_word != right_en_word:
        score += 1
        save_progres()
    else:
        score -= 1

    reset_card()


open_csv()
get_words()
get_en_word()

# Window
win = Tk()
win.title(f"Flashy - Score: {score}")
win.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# Card Button
f_c_img = PhotoImage(file="images/card_front.png")
b_c_img = PhotoImage(file="images/card_back.png")
card_button = Button(image=f_c_img, highlightthickness=0, width=800, height=526, background=BACKGROUND_COLOR,
                     command=turn_card)
card_button.grid(column=0, row=0, columnspan=2)

# Language Label
lan_lab = Label(text="French", font=("Arial", 40, "italic"))
lan_lab.place(x=400, y=150, anchor=CENTER)

# Word Label
word_lab = Label(text=fr_word, font=("Arial", 60, "bold"))
word_lab.place(x=400, y=263, anchor=CENTER)

# Wrong Button
w_img = PhotoImage(file="images/wrong.png")
w_butn = Button(image=w_img, highlightthickness=0, command=wrong_button)
w_butn.grid(column=0, row=1)

# Right Button
r_img = PhotoImage(file="images/right.png")
r_butn = Button(image=r_img, highlightthickness=0, command=right_button)
r_butn.grid(column=1, row=1)

win.mainloop()
