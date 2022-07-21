import smtplib
import datetime as dt
from random import choice


def sendmail(message):
    my_email = "email"
    password = "password"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Motivational quote\n\n{message}."
        )


now = dt.datetime.now()
if now.weekday() == 5:
    with open("./quotes.txt", mode="r") as file:
        quotes = file.readlines()
        quote = choice(quotes)

sendmail(quote)