import requests
import smtplib

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


def get_change():
    alp_function = "GLOBAL_QUOTE"
    alp_api_key = "api_key"

    alphavantage_api = f"https://www.alphavantage.co/query?function={alp_function}&symbol={STOCK}&apikey={alp_api_key}"
    stocks = requests.get(alphavantage_api)
    stocks.raise_for_status()
    difference = stocks.json()['Global Quote']["10. change percent"]
    difference = float(difference[0:len(difference) - 2])
    return difference


def get_news():
    news_api = "https://newsapi.org/v2/everything"
    params = {
        "apiKey": "api_key",
        "q": "Tesla",
        "pageSize": 3
    }
    news = requests.get(news_api, params=params)
    news.raise_for_status()
    news = news.json()['articles']
    return news


def sendmail(_state, _percent, _news):
    subject = f"{STOCK}: {state} {_percent}%"

    message = f"Headline : {_news[0]['title']}\n{_news[0]['description']}\n"
    message += f"\n\nHeadline : {_news[1]['title']}\n{_news[1]['description']}\n"
    message += f"\n\nHeadline : {_news[2]['title']}\n{_news[2]['description']}"

    my_email = "email"
    password = "password"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:{subject}\n\n{message}.".encode('utf-8')
        )


change = round(get_change())
state = ""
if -4 >= change or change >= 5:
    if change > 4:
        state = "↑"
    elif change <= -5:
        state = "↓"
    news = get_news()
    sendmail(state, change, news)
