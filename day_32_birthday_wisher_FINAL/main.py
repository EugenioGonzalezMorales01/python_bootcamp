import random
import pandas
from datetime import *
from smtplib import *


def get_data():
    with open("birthdays.csv") as file:
        return pandas.read_csv(file)


def get_letter(rand):
    with open(f"letter_templates/letter_{rand}.txt") as file:
        return file.read()


def send_mail(name, email):
    my_email = "eugenio.de.astora@gmail.com"
    password = "mxenjbgvqivxmpst"
    server = "smtp.gmail.com"
    tls_port = 587

    rand = random.randint(1, 3)
    letter = get_letter(rand).replace("[NAME]", f"{name}").replace("Angela", "Eugenio")

    with SMTP(server, tls_port) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"Subject:Happy Birthday!\n\n{letter}")
    return "Email Sent"


def check_birthdays():
    # Getting today's date
    today = datetime.now()
    today_tuple = (today.month, today.day)

    # Getting birthday's info - month and day as key
    data = get_data()
    birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

    if today_tuple in birthday_dict:
        print(send_mail(birthday_dict[today_tuple]["name"], birthday_dict[today_tuple]["email"]))
    else:
        print(f"today is no one's birthday")


check_birthdays()
