import pandas
import datetime as dt
import random
import smtplib


def sendmail(_email, _wish):
    my_email = "email"
    password = "password"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=_email,
            msg=f"Subject:Happy birthday!\n\n{_wish}."
        )


today = dt.datetime.now()
day = today.day
month = today.month

name = ""
email = ""
has_birthday = False
b_day_list = pandas.read_csv("birthdays.csv")
for index, row in b_day_list.iterrows():
    if row["day"] == day:
        if row["month"] == month:
            has_birthday = True
            name = row["name"]
            email = row["email"]

# 3. If step 2 is true, pick a random letter from letter templates and replace the
# [NAME] with the person's actual name from birthdays.csv


if has_birthday:
    with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt", "r") as file:
        wish = file.read()
    wish = wish.replace("[NAME]", name)
    sendmail(email, wish)
