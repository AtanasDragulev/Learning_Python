import random
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random", methods=["GET"])
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all", methods=["GET"])
def all_cafes():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


@app.route("/search", methods=["GET"])
def search():
    loc = request.args.get("loc")
    print(loc)
    cafes = db.session.query(Cafe).filter_by(location=loc).all()
    if cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes])
    return {"error": {"Not Found": "Sorry, we don`t have a cafe at that location."}}


@app.route("/add", methods=["POST"])
def add():
    api_key = request.args.get("api-key")
    if api_key != "TopSecretAPIKey":
        return {"error3": "Sorry, that`s not allowed. Make sure you have the correct api key."}, 403
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        has_sockets=bool(request.form.get("has_sockets")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        coffee_price=request.form.get("coffee_price"),
    )
    try:
        db.session.add(new_cafe)
        db.session.commit()
    except Exception as error:
        return {"response": {"error": "{}".format(error)}}
    return {"response": {"success": "Successfully added the new cafe."}}


@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    print(cafe.id, cafe.name)
    if cafe:
        new_price = request.args.get("new_price")
        cafe.coffee_price = new_price
        db.session.commit()
        return {"success": "Successfully updated the price."}
    return {"error": {"Not Found": "Sorry. A cafe with that id was not found in the database."}}


@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key != "TopSecretAPIKey":
        return {"error3": "Sorry, that`s not allowed. Make sure you have the correct api key."}, 403
    cafe = Cafe.query.get(cafe_id)
    if not cafe:
        return {"error": {"Not Found": "Sorry a cafe with that id was not found in the database."}}, 404
    db.session.delete(cafe)
    db.session.commit()
    return {"success": "Successfully deleted the cafe."}


if __name__ == '__main__':
    app.run(debug=True)
