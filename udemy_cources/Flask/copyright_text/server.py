from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route('/')
def home_page():
    year = str(datetime.date.today().year)
    name = "Atanas"
    return render_template('index.html', year=year, name=name)


if __name__ == '__main__':
    app.run()
