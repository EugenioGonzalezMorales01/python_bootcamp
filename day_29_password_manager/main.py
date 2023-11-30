import tkinter.messagebox
from tkinter import *
import pgc
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator_button():
    pass_entry.delete(0, END)
    pass_entry.insert(0, pgc.generate_password())
    pyperclip.copy(pass_entry.get())
# ---------------------------- SAVE PASSWORD ------------------------------- #

def generate_password():
    pass
def check_empty_entries():
    if wb_entry.get() == "" or user_entry.get() == "" or pass_entry.get() == "":
        return False
    else:
        return True

def save_entries():
    if check_empty_entries():
        website = wb_entry.get()
        user = user_entry.get()
        password = pass_entry.get()
        new_data = {
            website : {
                "email": user,
                "password": password
            }
        }
        desition = tkinter.messagebox.askyesno(title="Are you sure?", message=f"This is the saving data:\nWebsite: {website}\nemail/user :{user}\npassword :{password}")
        if desition:
            try:
                with open("info/user_info.json", "r") as user_info:
                    info = json.load(user_info)
            except FileNotFoundError:
                info = new_data
            else:
                info.update(new_data)
            finally:
                with open("info/user_info.json", "w") as user_info:
                    json.dump(info, user_info, indent=4)
                    wb_entry.delete(0, END)
                    pass_entry.delete(0, END)
    else:
        tkinter.messagebox.showwarning(title="Empty fields", message="You have to fill all the fields")

def search_wb():
    website = wb_entry.get()
    try:
        with open("info/user_info.json", "r") as user_info:
            data = json.load(user_info)
            data = {key: data[key] for key in data if key == website}
            print(data)
            tkinter.messagebox.showinfo(title=f"{website} Info", message=f"email: {data[website]['email']}\npassword: {data[website]['password']}")
    except KeyError:
        tkinter.messagebox.showerror(title="Name Error", message=f"{website} is not registered")
    except FileNotFoundError:
        tkinter.messagebox.showerror(title="No Saved Websites", message="You have not registered any website yet")
# ---------------------------- UI SETUP ------------------------------- #

# Window
win = Tk()
win.title("Password Generator")
win.config(padx=20, pady=20)

# Canvas
canv = Canvas(width=200, height=200, highlightthickness=0)
img = PhotoImage(file="logo.png")
canv.create_image(100, 100, image=img)
canv.grid(column=1, row=0)


# ----- Website -----
# Label
wb_label = Label(text="Website:")
wb_label.grid(column=0, row=1)

# Entry
wb_entry = Entry(width=35)
wb_entry.grid(column=1, row=1)
wb_entry.focus()

# Button
wb_button = Button(text="Search", command=search_wb)
wb_button.grid(column=2, row=1)

# ----- Email/UserName -----
#Label
user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)

#Entry
user_entry = Entry(width=35)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0,"eugenio.g.m@outlook.es")

# ----- Password ------
# Label
pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

# Entry
pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3)

#Button
pass_butt = Button(text="Generate Password", command=password_generator_button)
pass_butt.grid(column=2, row=3)

# ----- Send Button ------
#Button
send_butt = Button(text="Add", width=36, command=save_entries)
send_butt.grid(column=1, row=4, columnspan=2)


win.mainloop()