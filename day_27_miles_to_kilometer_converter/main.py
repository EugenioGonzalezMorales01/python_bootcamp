from tkinter import *

def ml_to_km():
    km = float(entry.get()) * 1.609344
    print(km)
    mtk_label.config(text=str(km))

# Window
win = Tk()
win.title("Mile to Km Converter")
win.minsize(width=300, height=200)

# Entry
entry = Entry()
entry.grid(column=1, row=0)

# Label "MIles"
label1 = Label(text="Miles")
label1.grid(column=2, row=0)

# Label "is equal to"
label2 = Label(text="is equal to")
label2.grid(column=0, row=1)

# Label "Miles to Km"
mtk_label = Label()
mtk_label.grid(column=1, row=1)

# Label "Km"
label3 = Label(text="Km")
label3.grid(column=2, row=1)

#Button
mtk_button = Button(text="Calculate", command=ml_to_km)
mtk_button.grid(column=1, row=2)

win.mainloop()