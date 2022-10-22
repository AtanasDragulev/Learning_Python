from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/guess/<user>")
def guess_genders(user):
    answer = requests.get(f"https://api.genderize.io?name={user}").json()
    user = str(user).title()
    gender = answer["gender"]
    probability = answer["probability"]
    return render_template("index.html", name=user, gender=gender, probability=probability)


while __name__ == '__main__':
    app.run(debug=True)
