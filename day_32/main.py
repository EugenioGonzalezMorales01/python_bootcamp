import random
import smtplib
import datetime as dt
my_email = "eugenio.de.astora@gmail.com"
my_password = "kjiotssxhqmjfcfu"

with open("quotes.txt") as file:
    data = file.readlines()
    data = random.choice(data)


with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    #This line will make our connection secure
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="just_eugene@hotmail.com",
                        msg=f"Subject:Hi beauty\n\n{data}")

birth_day = dt.datetime(year=2000, month=9, day=1, hour=12)

